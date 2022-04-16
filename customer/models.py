from datetime import timezone

from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=30)
    birthdate = models.DateField()
    email = models.EmailField(max_length=200)
    gender = models.BooleanField(default=True, null=True)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name + '(' + str(self.id) + ')'

