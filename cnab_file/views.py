from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from .models import CnabFile
from store.models import Store
import ipdb
from .serializers import CnabFileSerializer
from rest_framework import generics


class CnabView(generics.ListCreateAPIView):
    serializer_class = CnabFileSerializer
    queryset = CnabFile.objects.all()

    def perform_create(self, serializer):
        file = self.request.FILES['file'].read().decode().splitlines()

        for transaction in file:

            data_store = {
                'owner': transaction[48:62].strip(),
                'name': transaction[62:81].strip()
            }

            data_transaction = {
                'transaction_type': transaction[0:1],
                'date': f'{transaction[1:5]}-{transaction[5:7]}-{transaction[7:9]}',
                'value': 0,
                'cpf': transaction[19:30],
                'card': transaction[30:42],
                'hour': f'{transaction[42:44]}:{transaction[44:46]}:{transaction[46:48]}',
            }

            store, _ = Store.objects.get_or_create(**data_store)

            if transaction[0:1] == '1':
                data_transaction['transaction_type'] = 'Débito'
                data_transaction['value'] = +(int(transaction[9:19])/100.00)
            elif transaction[0:1] == '2':
                data_transaction['transaction_type'] = 'Boleto'
                data_transaction['value'] = -(int(transaction[9:19])/100.00)
            elif transaction[0:1] == '3':
                data_transaction['transaction_type'] = 'Financiamento'
                data_transaction['value'] = -(int(transaction[9:19])/100.00)
            elif transaction[0:1] == '4':
                data_transaction['transaction_type'] = 'Crédito'
                data_transaction['value'] = +(int(transaction[9:19])/100.00)
            elif transaction[0:1] == '5':
                data_transaction['transaction_type'] = 'Recebimento Empréstimo'
                data_transaction['value'] = +(int(transaction[9:19])/100.00)
            elif transaction[0:1] == '6':
                data_transaction['transaction_type'] = 'Vendas'
                data_transaction['value'] = +(int(transaction[9:19])/100.00)
            elif transaction[0:1] == '7':
                transaction_type = 'Recebimento TED'
                data_transaction['value'] = +(int(transaction[9:19])/100.00)
            elif transaction[0:1] == '8':
                data_transaction['transaction_type'] = 'Recebimento DOC'
                data_transaction['value'] = +(int(transaction[9:19])/100.00)
            elif transaction[0:1] == '9':
                data_transaction['transaction_type'] = 'Aluguel'
                data_transaction['value'] = -(int(transaction[9:19])/100.00)

            CnabFile.objects.create(**data_transaction, store=store)
