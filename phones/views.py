from audioop import reverse
from django.shortcuts import render, redirect
from phones.models import Phone
from django.http import HttpResponse


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    
    sort = request.GET.get('sort')
    phone_objects = Phone.objects.all()
    if sort == 'name':
        context = {'phones': phone_objects.order_by('name')}
    elif sort == 'min_price':
        context = {'phones': phone_objects.order_by('price')}
    else:
        context = {'phones': phone_objects.order_by('price').reverse}     
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    phone_object = Phone.objects.filter(slug=slug)
    for p in phone_object:
    
        context = {'phone': p}
    return render(request, template, context)



