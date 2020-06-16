from django.shortcuts import render

# Create your views here.

def index(request):

    data ={

    }

    return render(request, 'index.html', data)


def propos(request):
    
    data ={

    }

    return render(request,'about.html', data)



def contact(request):
    
    data ={

    }

    return render(request, 'contact.html', data)