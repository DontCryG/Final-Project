from django.shortcuts import render
from django.http import HttpResponse
from .models import SupportMessage

def Home(request):
    return render(request,'home/home.html')

def Services(request):
    return render(request,'home/service.html')

def Support(request):
    
    context = {}
    
    if request.method == 'POST':
        data = request.POST.copy()
        report = data.get('report')
        email = data.get('email')
        details = data.get('details')
        
        if report == '' or email == '':
            context['status'] = 'alert'
            return render(request,'home/support.html', context)
        
        new = SupportMessage()
        new.report = report
        new.email = email
        new.details = details
        new.save()
        context['status'] = 'success'
        
    return render(request,'home/support.html', context)