from rest_framework import serializers
from .models import InvestmentModel


class InvestmentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentModel
        fields = ('user_id', 'inputA', 'inputB', 'inputC', 'inputD', 'inputE')

    user_id = serializers.CharField(max_length=15)
    inputA = serializers.FloatField()
    inputB = serializers.IntegerField()
    inputC = serializers.IntegerField()
    inputD = serializers.IntegerField()
    inputE = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new InvestmentModel instance, given the validated data.
        """
        return InvestmentModel.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing InvestmentModel instance, given the validated data.
    #     """
    #     instance.user_id = validated_data.get('user_id', instance.user_id)
    #     instance.inputA = validated_data.get('inputA', instance.inputA)
    #     instance.inputB = validated_data.get('inputB', instance.inputB)
    #     instance.inputC = validated_data.get('inputC', instance.inputC)
    #     instance.inputD = validated_data.get('inputD', instance.inputD)
    #     instance.inputE = validated_data.get('inputE', instance.inputE)
    #     instance.save()
    #     return instance
