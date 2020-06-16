from django.shortcuts import render

# Create your views here.

def services(request):

    data = {

    }
    return render(request, 'services.html', data)

def apartment(request):
    
    data = {

    }
    return render(request, 'apartment.html', data)


def project(request):
    
    data = {

    }
    return render(request, 'project.html', data)

def elements(request):
    
    data = {

    }
    return render(request, 'elements.html', data)