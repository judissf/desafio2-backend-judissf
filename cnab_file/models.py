from django.db import models


class CnabFile(models.Model):
    transaction_type = models.CharField(max_length=22)

    date = models.DateField()

    value = models.DecimalField(max_digits=12, decimal_places=2)

    cpf = models.CharField(max_length=11)

    card = models.CharField(max_length=12)

    hour = models.TimeField()

    store = models.ForeignKey('store.Store', on_delete=models.CASCADE, related_name='transactions')

    