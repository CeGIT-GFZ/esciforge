from django.shortcuts import render
from publish.models import Submission,Author,Affiliation
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")


