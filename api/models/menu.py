from django.db import models

from api.models.restaurant import Restaurant


class Menu(models.Model):
    """
    Menu model
    """
    name = models.CharField(max_length=30)
    date = models.DateField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="menus")

    class Meta:
        unique_together = ("date", "restaurant"),
        indexes = [
            models.Index(fields=['date'])
        ]

    def __str__(self):
        return "Menu(name: {0}, date: {1}, restaurant: {2})".format(self.name, self.date, self.restaurant)
