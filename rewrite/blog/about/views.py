from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    response = render(request,'about.html')
    return response