from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json
from django.contrib.auth.forms import UserCreationForm

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
def static_page(request):
    return render(request, 'djangoapp/navbar.html')

# Create an `about` view to render a static about page
def about(request):
    return render(request, 'djangoapp/about.html')



# Create a `contact` view to return a static contact page
def contact(request):
    return render(request, 'djangoapp/contact.html')

# Create a `login_request` view to handle sign in request
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in.')
            return redirect('djangoapp:index')
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')

    return redirect('djangoapp:index')

# Create a `logout_request` view to handle sign out request
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('djangoapp:index')

# Create a `registration_request` view to handle sign up request
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('djangoapp:index')
    else:
        form = UserCreationForm()
    return render(request, 'djangoapp/registration.html', {'form': form})

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

