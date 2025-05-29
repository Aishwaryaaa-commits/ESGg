from django.db import models

class Company(models.Model):
    SECTOR_CHOICES = [
        ('Energy', 'Energy'),
        ('Finance', 'Finance'),
        ('Tech', 'Technology'),
        ('Healthcare', 'Healthcare'),
        ('Retail', 'Retail'),
        # Add more as needed
    ]

    name = models.CharField(max_length=200)
    location = models.CharField(max_length=500)
    sector = models.CharField(max_length=200, choices=SECTOR_CHOICES)
    reporting_time = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BusinessUnit(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='business_units')
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    function = models.CharField(max_length=255, help_text="What this unit does (e.g., Manufacturing, Sales)")

    def __str__(self):
        return f"{self.name} ({self.company.name})"


class Metric(models.Model):
    CATEGORY_CHOICES = [
        ('E', 'Environmental'),
        ('S', 'Social'),
        ('G', 'Governance'),
    ]

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class MetricValue(models.Model):
    business_unit = models.ForeignKey(BusinessUnit, on_delete=models.CASCADE, related_name='metric_values')
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE, related_name='values')
    reporting_period = models.CharField(max_length=100)  # e.g., "2023", "Q1 2024"
    value = models.FloatField()
    unit = models.CharField(max_length=50, help_text="e.g., kWh, %, incidents")

    def __str__(self):
        return f"{self.metric.name} - {self.business_unit.name} ({self.reporting_period})"
