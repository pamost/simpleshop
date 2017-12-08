from django.shortcuts import render
from .forms import *
from products.models import *


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    products_images_programms = products_images.filter(product__category_id=1)
    products_images_childs = products_images.filter(product__category_id=2)
    return render(request, 'landing/home.html', locals())


def landing(request):
    form = SubscriberForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)

        data = form.cleaned_data
        print(data['name'])

        form.save()

    return render(request, 'landing/landing.html', locals())
