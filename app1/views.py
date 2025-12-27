from django.shortcuts import render
from .models import user_details


# Create your views here.

def index(request):
    return render(request,'app1/index.html')

def login(request):
        return render(request,'app1/login.html')

def register_user(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Save data to database
        user = user_details(
            firstname=firstname,
            lastname=lastname,
            dob=dob,
            email=email,
            password=password
        )
        user.save()
