from django.shortcuts import render
from .models import Photo
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    i = random.randint(0, 1001)
    photos = Photo.objects.all()[i: i+100]
    return render(request, 'index.html', {'photos': photos})

def photos(request):
    photos_list = Photo.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(photos_list, 60)
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'photos.html', {'photos': photos})
