from rest_framework import serializers
from .models import Store
import ipdb


class StoreSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField()

    def get_balance(self, obj):
        all_values = obj.transactions.values('value')

        balance = 0

        for transaction_value in all_values:
            balance = balance + transaction_value['value']
        
        return balance
    
    class Meta:
        model = Store

        fields = [
            'owner',
            'name',
            'balance'
        ]    