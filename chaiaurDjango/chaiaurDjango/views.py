from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("Hello world. You are in home page")
    return render(request, 'website/index.html')

