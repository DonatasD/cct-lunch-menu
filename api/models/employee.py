from django.db import models


class Employee(models.Model):
    """
    Employee model
    """
    name = models.CharField(max_length=30)

    def __str__(self):
        return "Employee(name: {0})".format(self.name)
