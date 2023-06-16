from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    layout = models.ImageField(upload_to="restaurant_layouts")
    address = models.CharField(max_length=100, default="nowhere")
    description = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    opening_hours = models.CharField(max_length=100, default="10:00-22:00")

    def __str__(self):
        return self.name


class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    capacity = models.IntegerField(default=4)
    position_x = models.IntegerField(default=0)
    position_y = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.restaurant.name} - {self.id}"


class Reservation(models.Model):
    class State(models.TextChoices):
        INACTIVE = "IN", _("Inactive")
        ACTIVE = "AC", _("Active")
        COMPLETED = "CP", _("Completed")
        CANCELLED = "CN", _("Cancelled")

    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=2, choices=State.choices, default=State.INACTIVE)

    def __str__(self):
        return f"{self.table.restaurant.name} - {self.table.id} - {self.start} - {self.end}"
