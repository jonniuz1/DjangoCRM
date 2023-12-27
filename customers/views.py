from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View

from .models import Customer
from .forms import SignUpForm, CustomerForm


@login_required
def home(request):
    customers = Customer.active.all()
    return render(request, 'customers/home.html', {'customers': customers})


@login_required
def customer(request, pk):
    customer = Customer.active.get(pk=pk)
    return render(request, 'customers/customer.html', {'customer': customer})


@login_required
def add_customer(request):
    form = CustomerForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'New customer has been added...')
            return redirect('home')

    else:
        return render(request, 'customers/add-customer.html', {'form': form})


@login_required
def update_customer(request, pk):
    current_customer = Customer.objects.get(pk=pk)
    form = CustomerForm(request.POST or None, instance=current_customer)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, f"Customer '{current_customer}' has been updated...")
            return redirect('home')

    return render(request, 'customers/add-customer.html', {'form': form, 'customer': current_customer})


class DeleteView(View):
    template_name = 'customers/delete-customer.html'

    def post(self, request, pk):
        current_customer = Customer.objects.get(pk=pk)
        current_customer.delete()
        print(f"Delete Post: {request.method}")
        messages.info(request, "You have successfully deleted the '{}'".format(current_customer))
        return redirect("home")

    def get(self, request, pk):
        current_customer = Customer.objects.get(pk=pk)
        print(f"Delete Get: {request.method}")
        return render(request, self.template_name, {'customer': current_customer})


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, f'You have been logged in as "{username}" successfully...')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registrations/register.html', {'form': form})


def login_customer(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'You logged in as "{username}" successfully...')
            return redirect('home')
        else:
            messages.info(request, 'Something went wrong... Please try again!')
            return redirect('login')
    return render(request, 'registrations/login.html')


@login_required
def logout_customer(request):
    messages.info(request, 'You have been logged out...')
    logout(request)
    return redirect('home')
