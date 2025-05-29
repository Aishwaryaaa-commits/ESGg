# breathesg/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, this is my ESG homepage!")

