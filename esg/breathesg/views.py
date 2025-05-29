from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Company, BusinessUnit, Metric, MetricValue
from .serializers import CompanySerializer, BusinessUnitSerializer, MetricSerializer, MetricValueSerializer

# Generic view template
class BaseModelView(APIView):
    model = None
    serializer_class = None

    def get(self, request, pk=None):
        if pk:
            instance = get_object_or_404(self.model, pk=pk)
            serializer = self.serializer_class(instance)
        else:
            instances = self.model.objects.all()
            serializer = self.serializer_class(instances, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        instance = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        instance = get_object_or_404(self.model, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CompanyView(BaseModelView):
    model = Company
    serializer_class = CompanySerializer

class BusinessUnitView(BaseModelView):
    model = BusinessUnit
    serializer_class = BusinessUnitSerializer

class MetricView(BaseModelView):
    model = Metric
    serializer_class = MetricSerializer

class MetricValueView(BaseModelView):
    model = MetricValue
    serializer_class = MetricValueSerializer
