from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from .models import CnabFile
import ipdb


class CnabView(APIView):
    def post(self, request: Request) -> Response:
        file = request.FILES['file'].read().decode().splitlines()

        for transaction in file:

            data = {
                'transaction_type': transaction[0:1],
                'date': f'{transaction[1:5]}-{transaction[5:7]}-{transaction[7:9]}',
                'value': 0,
                'cpf': transaction[19:30],
                'card': transaction[30:42],
                'hour': f'{transaction[42:44]}:{transaction[44:46]}:{transaction[46:48]}',
                'owner': transaction[48:62],
                'store_name': transaction[62:81]
            }

            if transaction[0:1] == '1':
                data['transaction_type'] = 'Débito'
                data['value'] = +(int(transaction[9:19])/100.00)
            elif transaction[0:1] == '2':
                data['transaction_type'] = 'Boleto'
                data['value'] = -(int(transaction[9:19])/100.00)
            elif transaction[0:1] == '3':
                data['transaction_type'] = 'Financiamento'
                data['value'] = -(int(transaction[9:19])/100.00)
            elif transaction[0:1] == '4':
                data['transaction_type'] = 'Crédito'
                data['value'] = +(int(transaction[9:19])/100.00)
            elif transaction[0:1] == '5':
                data['transaction_type'] = 'Recebimento Empréstimo'
                data['value'] = +(int(transaction[9:19])/100.00)
            elif transaction[0:1] == '6':
                data['transaction_type'] = 'Vendas'
                data['value'] = +(int(transaction[9:19])/100.00)
            elif transaction[0:1] == '7':
                transaction_type = 'Recebimento TED'
                data['value'] = +(int(transaction[9:19])/100.00)
            elif transaction[0:1] == '8':
                data['transaction_type'] = 'Recebimento DOC'
                data['value'] = +(int(transaction[9:19])/100.00)
            elif transaction[0:1] == '9':
                data['transaction_type'] = 'Aluguel'
                data['value'] = -(int(transaction[9:19])/100.00)

            CnabFile.objects.create(
                transaction_type=data['transaction_type'],
                date=data['date'],
                value=data['value'],
                cpf=data['cpf'],
                card=data['card'],
                hour=data['hour'],
                owner=data['owner'],
                store_name=data['store_name']
            )

        return Response(status=status.HTTP_201_CREATED, data={'message': 'Data registered successfully.'})

    def get(self, request: Request) -> Response:
        transactions = CnabFile.objects.all()

        return Response(status=status.HTTP_200_OK, data=transactions)
