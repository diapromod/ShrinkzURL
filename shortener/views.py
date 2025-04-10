from django.shortcuts import render, redirect, get_object_or_404
from .models import URL
from django.http import HttpResponse

def home(request):
    if request.method == 'POST':
        original_url = request.POST['long_url']
        url, created = URL.objects.get_or_create(original_url=original_url)
        short_url = request.build_absolute_uri(f'/{url.short_code}')
        return render(request, 'shortener/shortened.html', {'short_url': short_url})
    return render(request, 'shortener/home.html')


def redirect_url(request, code):
    url = get_object_or_404(URL, short_code=code)
    return redirect(url.original_url)
