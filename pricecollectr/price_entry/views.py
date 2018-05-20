import time

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from price_entry.models import Price


def index(request):
    return HttpResponse('This is the index view.')

def enter_price(request):
    if request.method == 'POST':
        new_entry = Price()
        new_entry.product_id = request.POST.get('product_id')
        new_entry.name = request.POST.get('name')
        new_entry.price = request.POST.get('price')
        new_entry.unit = request.POST.get('unit')
        new_entry.store = request.POST.get('store')
        new_entry.location =request.POST.get('location')
        new_entry.save()
        return redirect('/price_entry/good_submit')
    else:
        return render(request, 'price_entry/enter_price.html')

def good_submit(request):
    return render(request, 'price_entry/good_submit.html')

