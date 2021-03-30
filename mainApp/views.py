from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    image = Image.objects.all()
    cat = Category.objects.all()
    print(cat)
    context = {'images': image,'categories':cat}
    return render(request,'index.html',context)

def category(request,cid):
    cat = Category.objects.get(pk=cid)
    image = Image.objects.filter(cat=cat)
    category = Category.objects.all()
    print(cat)
    context = {'images': image,'categories':category}
    return render(request,'index.html',context)
