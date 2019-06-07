from __future__ import unicode_literals 
from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from .models import bus
from .forms import  UpdatebioForm,  NewsLetterForm,Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .permissions import IsAdminOrReadOnly
from rest_framework.views import APIView
# Create your views here.

@login_required(login_url='/accounts/login')

def home(request):
    # Display all projects here:

    if request.GET.get('search_term'):
        bus = bus.search_bus(request.GET.get('search_term'))

    else:
        bus = bus.objects.all()

    form = NewsLetterForm
    if request.method == 'POST':
        form = NewsLetterForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)

            HttpResponseRedirect('home')

    return render(request, 'index.html', {'bus':bus, 'letterForm':form})