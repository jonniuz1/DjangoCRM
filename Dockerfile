# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /usr/src/django-crm/

# Copy the requirements file into the container at /usr/src/app
COPY requirements.txt /usr/src/django-crm/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/django-crm/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run your application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]
