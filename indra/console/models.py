# console/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    zoneID = models.CharField(max_length=20, unique=True, blank=True, null=True)
    secretKey = models.CharField(max_length=100, blank=True, null=True)


class CSVData(models.Model):
    year = models.IntegerField(default=2023)  # Add year field
    month = models.CharField(max_length=20)
    day = models.IntegerField()
    real_losses = models.IntegerField()
    flow_analysis_central = models.DecimalField(max_digits=10, decimal_places=3)  # Updated to DecimalField
    flow_analysis_receive = models.DecimalField(max_digits=10, decimal_places=3)  # Updated to DecimalField
    loss_analysis = models.CharField(max_length=10)
    alert_analysis = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.year} - {self.month} - {self.day}"


class ClassifiedWaterFlowData(models.Model):
    year = models.IntegerField()
    month = models.CharField(max_length=20)
    total_real_losses = models.DecimalField(max_digits=10, decimal_places=2)
    total_flow_analysis_central = models.DecimalField(max_digits=10, decimal_places=3)
    total_flow_analysis_receive = models.DecimalField(max_digits=10, decimal_places=3)
    
    system_input_volume = models.DecimalField(max_digits=10, decimal_places=2,default=9000)
    build_consumer = models.DecimalField(max_digits=10, decimal_places=2,default=7500)
    non_revenue_water = models.DecimalField(max_digits=10, decimal_places=2,default=1000)
    arbitrary_loss = models.FloatField(default=300)
    unauthorised_consumption = models.FloatField(default=400)

    def __str__(self):
        return f"{self.year} - {self.month}"
    

