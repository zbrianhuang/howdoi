from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import os
# Create your views here.

class blogs(TemplateView):
    template_name = "blogtemplate.html"

def index(request):
    response = render(request,'index.html')
    return response