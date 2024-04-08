from django.shortcuts import render
from .models import UserDetails
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'Portfolio/home.html')
def abt(request):
    return render(request, 'Portfolio/about.html')
def project(request):
    return render(request, 'Portfolio/projects.html')
def contact(request):
    message = None  # Initialize the message variable

    if request.method == 'POST':
        user = UserDetails()
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        message_content = request.POST.get('message')
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.contact_number = contact_number
        user.message = message_content
        user.save()
        message = 'Thank you for contacting us! We will get back to you shortly.'

    return render(request, 'Portfolio/contact.html', {'message': message})