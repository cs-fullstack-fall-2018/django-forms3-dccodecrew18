from django.db import models
from datetime import datetime


class FormModel(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    opsbudget = models.CharField(max_length=300)
    numberemployees = models.IntegerField()
    estdate = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name, self.address, self.opsbudget, self.numberemployees, self.estdate