from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from images.models import User_Image
from images.forms import ImageForm

def index(request):
    images = User_Image.objects.filter(is_public=True).order_by('-uploaded_at')[:3]
    return render(request, 'images/index.html', { 'images': images })

def model_form_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ImageForm()
    return render(request, 'images/model_form_upload.html', {
        'form': form
    })