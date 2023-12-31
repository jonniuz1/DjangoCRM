from django.db import models


class CustomerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Customer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    objects = models.Manager()
    active = CustomerManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
