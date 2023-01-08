from django.shortcuts import render

# Create your views here.

def newfile(request):
    return render(request,'newfile.html')