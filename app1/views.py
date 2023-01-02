from django.shortcuts import render

def highest(request):
    d={'a':10 , 'b':20 , 'c':30}
    return render(request,'highest.html',d)
    
