from rest_framework import serializers


class StatisticSerializer(serializers.Serializer):
    product_count = serializers.IntegerField()
    total = serializers.DecimalField(max_digits=10, decimal_places=2)
    username = serializers.CharField(max_length=30)

