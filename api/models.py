from django.db import models


# Model for Employee
class Employee(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return "Employee(name: {0})".format(self.name)
