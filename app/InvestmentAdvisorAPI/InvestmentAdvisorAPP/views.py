from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import InvestmentModel
from .serializers import InvestmentModelSerializer
from django.http import Http404
import json


class InvestmentView(APIView):
    """
    Add, retrieve a instance

    """
    def post(self, request):
        data = request.data
        # print(data)
        serializer = InvestmentModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            sum = self.calSum(data)
            label = self.generateLabel(sum)
            if label:
                # print(json.dumps(label))
                j = json.dumps(label)
                j = json.loads(j)
                return Response(j, content_type = 'application/json')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def calSum(self, query_dic):
        sum = 0
        sum += float(query_dic['inputA'][0])
        sum += float(query_dic['inputB'][0])
        sum += float(query_dic['inputC'][0])
        sum += float(query_dic['inputD'][0])
        sum += float(query_dic['inputE'][0])
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
            return 0
