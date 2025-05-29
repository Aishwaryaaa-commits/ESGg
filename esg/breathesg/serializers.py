from rest_framework import serializers
from .models import Company, BusinessUnit, Metric, MetricValue

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class BusinessUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessUnit
        fields = '__all__'

class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = '__all__'

class MetricValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetricValue
        fields = '__all__'
