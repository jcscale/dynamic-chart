from django.db.models import fields
from rest_framework import serializers
from chart.models import Chart


class ChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chart
        fields = ['number', 'date']
