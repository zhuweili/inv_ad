from django.db import models


class InvestmentModel(models.Model):
    user_id = models.CharField(max_length=15)
    inputA = models.FloatField()
    inputB = models.IntegerField()
    inputC = models.IntegerField()
    inputD = models.IntegerField()
    inputE = models.IntegerField()

    def __str__(self):
        return self.user_id


class RiskModel(models.Model):
    user_id = models.CharField(max_length=15)
    user_FICO = models.IntegerField()
    BorrowerExp = models.IntegerField()
    LTV = models.FloatField()
    PersonalGuarantee = models.BooleanField()
    Coupon = models.FloatField()
    Grade = models.CharField(max_length=5)

    def __str__(self):
        return self.user_id


class ExpModel(models.Model):
    user_id = models.CharField(max_length=15)
    transactionNumEver = models.IntegerField()
    transactionNum12 = models.IntegerField()
    transactionNum6 = models.IntegerField()
    transactionPurchaseEver = models.FloatField()
    transactionPurchase12 = models.FloatField()
    transactionPurchase6 = models.FloatField()

    def __str__(self):
        return self.user_id
