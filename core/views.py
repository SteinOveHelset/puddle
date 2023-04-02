from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm

from PIL import Image

import os

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    
    for item in items:
        
        path = os.getcwd() + item.image.url
        with Image.open(path) as img:
            # Resize the image to the desired dimensions
            resized_img = img.resize((5536, 4160))

            # Overwrite the original image with the resized image
            resized_img.save(path)

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
