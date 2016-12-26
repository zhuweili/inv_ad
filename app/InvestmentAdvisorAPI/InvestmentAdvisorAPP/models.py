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
