from faker import Faker
from .models import Customer
import json

fake = Faker()

def generate_customer(num):
	all_data = []
	for i in range(num):
		first_name = fake.first_name(),
		last_name = fake.last_name(),
		email = fake.email(),
		phone = fake.phone_number(),
		address = fake.address(),
		city = fake.city(),
		state = fake.country(),
		zipcode = fake.zipcode(),
		is_active = fake.boolean(chance_of_getting_true=25)
		# print((first_name[0]))
		data = dict({
			'first_name': first_name[0],
			'last_name': last_name[0],
			'email': email[0],
			'phone': phone[0],
			'address': address[0],
			'city': city[0],
			'state': state[0],
			'zipcode': zipcode[0],
			'is_active': is_active,
					 })

		customer = Customer.objects.create(
			first_name=first_name[0],
			last_name=last_name[0],
			email=email[0],
			phone=phone[0],
			address=address[0],
			city=city[0],
			state=state[0],
			zipcode=zipcode[0],
			is_active=is_active
			)
		customer.save()
		all_data.append(data)

	with open('dummy_customer.json', 'w') as f:
		json.dump(all_data, f, ensure_ascii=True, indent=4)

