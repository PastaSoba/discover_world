from django.db import models

# Create your models here.
class TouristSpot(models.Model):
    spot_name = models.CharField(max_length=100)
    country = models.CharField(max_length=20, null=True)
    prefecture = models.CharField(max_length=10, null=True)
    created_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.spot_name