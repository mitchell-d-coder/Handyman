from django.shortcuts import render, get_object_or_404


from .models import Post

# Create your views here.

def home(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request, 'gallery.html')


def blogs(request, slug):
    blog = get_object_or_404(Post, slug=slug)
    return render(request, 'blog-single.html', {'blog':blog})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'aboutus.html')

def services(request):
    return render(request, 'services.html')

def menu(request):
    return render(request, 'menu.html')
