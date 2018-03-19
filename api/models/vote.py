import logging

from django.db import models
from rest_framework.exceptions import ValidationError

from api.models.employee import Employee
from api.models.menu import Menu

logger = logging.getLogger(__name__)


class Vote(models.Model):
    """
    Vote model
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="votes")
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="menus")

    def validate_unique(self, exclude=None):
        qs = Vote.objects.filter(employee=self.employee, menu__date=self.menu.date)
        if qs.exists():
            error_type = "non_field_errors"
            error_message = "The fields employee, menu date must make a unique set."
            logging.error("Failed to save: {0} with error type: {1} and error message: {2}"
                          .format(self, error_type, error_message))
            raise ValidationError({
                error_type: [
                    error_message
                ]
            })

    def save(self, *args, **kwargs):
        self.validate_unique()
        super(Vote, self).save(*args, **kwargs)

    def __str__(self):
        return "Vote(employee: {0}, menu: {1})".format(self.employee, self.menu)
