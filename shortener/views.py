from django.shortcuts import render, redirect, get_object_or_404
from .forms import URLForm
from .models import URL

def home(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url_instance = form.save()
            return render(request, 'shortener/success.html', {'shortened_url': url_instance.shortened_url})
    else:
        form = URLForm()
    return render(request, 'shortener/home.html', {'form': form})

def redirect_url(request, shortened_url):
    url_instance = get_object_or_404(URL, shortened_url=shortened_url)
    return redirect(url_instance.original_url)
