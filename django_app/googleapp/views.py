from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def google_view(request):
    return render(request, 'google_view.html')