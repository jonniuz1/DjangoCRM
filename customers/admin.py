from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
	list_display = ['email', 'phone', 'address', 'state', 'created_at']

admin.site.register(Customer, CustomerAdmin)