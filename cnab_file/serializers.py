from rest_framework import serializers
from .models import CnabFile


class CnabFileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(write_only=True)
    
    class Meta:
        model = CnabFile

        fields = [
            'transaction_type',
            'date',
            'value',
            'cpf',
            'card',
            'hour',
            'file',
            'store'
        ]

        depth = 1

        read_only_fields = [
            'transaction_type',
            'date',
            'value',
            'cpf',
            'card',
            'hour',
            'store'
        ]

    def create(self, validated_data: dict) -> CnabFile:
        return CnabFile.objects.create(**validated_data)

    # transaction_type = serializers.CharField(read_only=True, max_length=22)
    # date = serializers.DateField(read_only=True, )
    # value = serializers.DecimalField(
    #     read_only=True, max_digits=12, decimal_places=2)
    # cpf = serializers.CharField(read_only=True, max_length=11)
    # card = serializers.CharField(read_only=True, max_length=12)
    # hour = serializers.TimeField(read_only=True, )
    # owner = serializers.CharField(read_only=True, max_length=100)
    # store_name = serializers.CharField(read_only=True, max_length=100)
