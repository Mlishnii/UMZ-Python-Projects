from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Profile

def CV(request):
    profiles = Profile.objects.all()
    template = loader.get_template('CV/CV.html')
    context = {'profiles': profiles}
    rendered_template = template.render(context,request)
    return HttpResponse(rendered_template) 
