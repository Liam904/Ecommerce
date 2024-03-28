from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

@login_required
def index(request):
    items = Item.objects.all()
    
    return render(request, 'dashboard/index.html', {
        'items':items,
    })

