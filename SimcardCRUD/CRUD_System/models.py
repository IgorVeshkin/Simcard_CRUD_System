from django.db import models

# Create your models here.


class TariffPlan(models.Model):
    Title = models.CharField(max_length=255)
    Minutes = models.CharField(max_length=20)
    SMS = models.CharField(max_length=20)
    Gigabytes = models.CharField(max_length=20)
    Price = models.IntegerField()

    def __str__(self):
        return self.Title


class Simcard(models.Model):
    IMEI = models.CharField(max_length=255)
    PhoneNumber = models.CharField(max_length=255, blank=False)
    ClientName = models.CharField(max_length=100)
    RegistrationDate = models.DateField()
    TariffPlan = models.ForeignKey(TariffPlan, on_delete=models.SET_NULL, null=True)
    RecordCreationTime = models.DateTimeField(auto_now_add=True)
    RecordUpdateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ClientName + ' ' + self.PhoneNumber