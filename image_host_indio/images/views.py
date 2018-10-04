from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

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

def specific_image(request, img_width, img_height):
	if int(img_width) < 0 or int(img_height) < 0:
		return HttpResponse("Oops! Looks like you input two invalid numbers, please imput real integers that are greater than 1") 
	image = User_Image.objects.filter(
		is_public=True, 
		image_width=img_width, 
		image_height=img_height).order_by('-uploaded_at')[:1]

	if not image:
		# return a different image who's dimensions are closest to those specified
		return HttpResponse("No image with dimensions found")
	return render(request, 'images/specific_image.html', {'image': image})