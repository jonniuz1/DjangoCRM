from django.core.management.base import BaseCommand
from ...utils import generate_customer

class Command(BaseCommand):
	help = "generate dummy data for customer"
	def handle(self, *args, **kwargs):
		generate_customer(15)
		print("Completed")