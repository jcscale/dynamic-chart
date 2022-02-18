from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.


class Chart(models.Model):
    number = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.number)
