from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import FileResponse
import os

@csrf_exempt
def index(request):
    return render(request, 'portfolio/index.html')
@csrf_exempt
def resume(request):
    return FileResponse(open('portfolio/static/oliver_whittlef_resume.pdf', 'rb'), content_type='application/pdf')
@csrf_exempt
def contact(request):
    return render(request, 'portfolio/contact.html')
