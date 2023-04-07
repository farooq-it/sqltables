from django.shortcuts import render

# Create your views here.
from app.models import *

def display_dept(request):
    LOD=Dept.objects.all()
    d={'gaga':LOD}
    return render(request,'display_dept.html',d)

def display_emp(request):
    LOE=Emp.objects.all()
    d={'gigi':LOE}
    return render(request,'display_emp.html',d)