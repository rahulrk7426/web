from django.shortcuts import render
from . models import place
from . models import inspects
# Create your views here.

def website(request):
    obj=place.objects.all()
    obj1 = inspects.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})



