from django.shortcuts import render

# Create your views here.
def blog(request):
    data = { 

    }

    return render(request, 'blog.html', data)




def single(request):
    data = { 

    }

    return render(request, 'single-blog.html', data)