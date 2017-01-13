from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import InvestmentModel
from .serializers import InvestmentModelSerializer
from .serializers import RiskModelSerializer
from .serializers import ExpModelSerializer
from django.http import Http404
import json


class InvestmentView(APIView):
    """
    Add, retrieve a instance

    """

    def post(self, request):
        data = request.data
        print(data)
        serializer = InvestmentModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            sum = self.calSum(data)
            label = self.generateLabel(sum)
            if label:
                # j = json.dumps(label)
                return Response(label, content_type='application/javascript; charset=utf8')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def calSum(self, query_dic):
        sum = 0
        sum += float(query_dic['inputA'])
        sum += float(query_dic['inputB'])
        sum += float(query_dic['inputC'])
        sum += float(query_dic['inputD'])
        sum += float(query_dic['inputE'])
        return sum

    def generateLabel(self, sum):
        if 0 < sum <= 5:
            return {'label': '1'}
        elif 5 < sum <= 10:
            return {'label': '2'}
        elif 10 < sum <= 15:
            return {'label': '3'}
        elif 15 < sum <= 20:
            return {'label': '4'}
        elif 20 < sum <= 25:
            return {'label': '5'}
        else:
            return {}


class RiskAndExpView(APIView):
    Coupon_MIN, LTV_MIN = 0.075, 0.57
    Grade_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    def post(self, request):
        data = request.data
        print(data)
        risk_data, exp_data, tier = {}, {}, -1
        # tier is borrow exp
        exp_data['user_id'] = data['user_id']
        exp_data['transactionNumEver'] = data['transactionNumEver']
        exp_data['transactionNum12'] = data['transactionNum12']
        exp_data['transactionNum6'] = data['transactionNum6']
        exp_data['transactionPurchaseEver'] = data['transactionPurchaseEver']
        exp_data['transactionPurchase12'] = data['transactionPurchase12']
        exp_data['transactionPurchase6'] = data['transactionPurchase6']
        tier = self.getTier(exp_data)

        exp_serializer = ExpModelSerializer(data=exp_data)
        if exp_serializer.is_valid():
            exp_serializer.save()
            if tier > 0:
                risk_data['BorrowerExp'] = tier
            else:
                return Response({'BorrowerExp': 'invalid BorrowerExp'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(exp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        risk_data['user_id'] = data['user_id']
        risk_data['user_FICO'] = data['user_FICO']
        risk_data['LTV'] = data['LTV']
        if float(risk_data['LTV']) < self.LTV_MIN or float(risk_data['LTV']) > 1:
            return Response({'LTV': 'LTV is supposed to be larger than 0.57 less than 1.'},
                            status=status.HTTP_400_BAD_REQUEST)

        if data['PersonalGuarantee'] == '1':
            risk_data['PersonalGuarantee'] = True
        else:
            risk_data['PersonalGuarantee'] = False
        temp = self.calCoupon(risk_data)
        risk_data['Coupon'] = temp[1]
        risk_data['Grade'] = temp[0]

        risk_serializer = RiskModelSerializer(data=risk_data)
        if risk_serializer.is_valid():
            risk_serializer.save()
            J = {}
            J['Coupon'] = risk_data['Coupon']
            J['Grade'] = risk_data['Grade']
            return Response(J, content_type='application/javascript; charset=utf8')
        return Response(risk_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def getTier(self, exp_data):
        number = int(exp_data['transactionNumEver'])
        if number < 0:
            return -1
        if number < 3:
            return 4
        if number < 25:
            return 3
        if number < 75:
            return 2
        else:
            return 1

    def calCoupon(self, risk_data):
        FICO = int(risk_data['user_FICO'])
        print('FICO', FICO)
        if FICO < 680:
            return 'Rej', -1.0
        LTV = float(risk_data['LTV'])
        personalGuarantee = risk_data['PersonalGuarantee']
        borrowerExp = int(risk_data['BorrowerExp'])
        gradeMap = self.generateGradeToCouponMap()
        grade = self.calGrade(LTV, borrowerExp)
        print(len(gradeMap), gradeMap)
        coupon = gradeMap[grade]
        if personalGuarantee == True:
            return grade, round(float(coupon), 3)
        else:
            return grade, round(float(coupon) + 0.01, 3)

    def generateGradeToCouponMap(self):
        temp = self.Coupon_MIN
        res = {}
        for letter in self.Grade_letters:
            for num in range(1, 6):
                res[letter + str(num)] = round(temp, 3)
                temp += float(0.002)
                temp = round(temp, 3)
        return res

    def calGrade(self, ltv, borrowerExp):
        ltv -= self.LTV_MIN
        ltv *= 100
        ltv += borrowerExp
        grade_letter = self.Grade_letters[int((int(ltv) - 1) / 5)]
        grade_number = ((int(ltv) - 1) % 5) + 1
        grade = grade_letter + str(grade_number)
        return grade
