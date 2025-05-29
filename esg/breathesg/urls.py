from django.urls import path
from .views import CompanyView, BusinessUnitView, MetricView, MetricValueView

urlpatterns = [
    path('companies/', CompanyView.as_view()),
    path('companies/<int:pk>/', CompanyView.as_view()),

    path('business-units/', BusinessUnitView.as_view()),
    path('business-units/<int:pk>/', BusinessUnitView.as_view()),

    path('metrics/', MetricView.as_view()),
    path('metrics/<int:pk>/', MetricView.as_view()),

    path('metric-values/', MetricValueView.as_view()),
    path('metric-values/<int:pk>/', MetricValueView.as_view()),

    path('admin/', admin.site.urls),
    path('', include('breatheesgb.urls')), 
]
