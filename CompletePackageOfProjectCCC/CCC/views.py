
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required as django_login_required
from django.contrib.auth.hashers import make_password, check_password
import logging
from .models import Registration, CreateUserLogin
from django.db.models import Q 
from .decorators import login_required_decorator 

def homepage(request):
    return render(request, 'CCC/homepage.html')

def LoginToReg(request):
    return render(request, 'CCC/loginToReg.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if CreateUserLogin.objects.filter(username=username).exists():            
            messages.error(request, "Username already exists")
            return redirect('signup')
        user = CreateUserLogin(username=username, password=make_password(password))
        user.save()
        
        return redirect('signin')
    return render(request, 'CCC/signup.html')

logger = logging.getLogger(__name__)

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('register')  
        else:
            messages.error(request, 'Invalid username or password')
            logger.error(f'Login failed for username: {username}')
    return render(request, 'CCC/signin.html')


def user_logout(request):
    logout(request)  # Logs out the user
    return redirect('homepage')

@login_required_decorator  # Use the custom login required decorator here
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        job_role = request.POST['job_role']
        locality = request.POST['locality']
        description = request.POST['description']
        phone = request.POST['phone']

        Registration.objects.create(
            name=name,
            job_role=job_role,
            locality=locality,
            description=description,
            phone=phone
        )
        return redirect('homepage')
    return render(request, 'CCC/register.html')

def search(request):
    return render(request, 'CCC/search.html')

def jobrole(request):
    job_roles = Registration.objects.values_list('job_role', flat=True).distinct()
    input_query = request.GET.get('job_role_input', '').strip().lower()
    dropdown_query = request.GET.get('job_role_dropdown', '').strip().lower()
    query = input_query if input_query else dropdown_query

    results = None
    if query:
        results = Registration.objects.filter(Q(job_role__icontains=query))

    return render(request, 'CCC/jobrole.html', {
        'job_roles': job_roles,
        'results': results
    })

def location(request):
    locations = Registration.objects.values_list('locality', flat=True).distinct()
    input_query = request.GET.get('location_input', '').strip().lower()
    dropdown_query = request.GET.get('location_dropdown', '').strip().lower()

    query = input_query if input_query else dropdown_query

    results = None
    if query:
        results = Registration.objects.filter(Q(locality__icontains=query))

    return render(request, 'CCC/location.html', {
        'locations': locations,
        'results': results
    })

def description(request):
    job_roles = Registration.objects.values_list('job_role', flat=True).distinct()
    input_query = request.GET.get('job_role_input', '').strip().lower()
    dropdown_query = request.GET.get('job_role_dropdown', '').strip().lower()
    query = input_query if input_query else dropdown_query

    results = None
    if query:
        results = Registration.objects.filter(Q(job_role__icontains=query))

    return render(request, 'CCC/description.html', {
        'job_roles': job_roles,
        'results': results
    })