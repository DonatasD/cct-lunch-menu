from django.db import models


class Restaurant(models.Model):
    """
    Restaurant model
    """
    name = models.CharField(max_length=30)

    def __str__(self):
        return "Restaurant(name: {0})".format(self.name)
