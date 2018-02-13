from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator


class Vehicles(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    vin_number = models.CharField(unique=True, max_length=17, blank=True, null=True,
                                  validators=[RegexValidator(r'^[0-9A-Z]{17}$')],
                                  error_messages={'unique': "VIN already exists"})
    make = models.CharField(max_length=15, blank=True, null=True)
    model = models.CharField(max_length=15, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    vehicle_type = models.CharField(max_length=8)

    class Meta:
        managed = True
        db_table = 'vehicles'

    def get_absolute_url(self):
        return reverse('vehicles:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.make + ' - ' + self.vin_number + ' - ' + self.vehicle_type



