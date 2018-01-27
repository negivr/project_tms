from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator


class People(models.Model):
    person_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField()
    # ssn = models.IntegerField(unique=True, blank=True, null=True)
    ssn = models.CharField(unique=True, max_length=9, validators=[RegexValidator(r'^[0-9]{9}$')], error_messages={
        'unique': "Check SSN. It probably already exists"})  # ogranicava broj cifara na 9, ne moze vise, ne moze manje

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        managed = True
        db_table = 'people'

    def get_absolute_url(self):
        return reverse('people:detail', kwargs={'pk': self.pk})

