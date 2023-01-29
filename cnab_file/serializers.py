from rest_framework import serializers

class CnabFile(serializers.Serializer):
    file = serializers.FileField(write_only=True)