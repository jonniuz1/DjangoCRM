from faker import Faker
from .models import Customer


fake = Faker()

def generate_customer(num):
	for i in range(num):
		customer = Customer.objects.create(first_name=fake.last_name(),
			last_name=fake.last_name(),
			email=fake.email(),
			phone=fake.phone_number(),
			address=fake.address(),
			city=fake.city(),
			state=fake.country(),
			zipcode=fake.zipcode(),
			is_active=True
			)
		customer.save()