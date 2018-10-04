from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db.models import Func, F
from django.http import HttpResponse

from images.models import User_Image
from images.forms import ImageForm

def index(request):
	# I keep the number of images displayed on the home page limited
	# so that I can keep the page less cluttered.

    images = User_Image.objects.filter(is_public=True).order_by('-uploaded_at')[:3]
    return render(request, 'images/index.html', { 'images': images })

def model_form_upload(request):

	# Code obtained and modified from: 
	# https://github.com/sibtc/simple-file-upload
	# Original Author: https://github.com/sibtc

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

# url looks like /images/<int>/<int>/
def specific_image(request, img_width, img_height):
	if int(img_width) < 0 or int(img_height) < 0:
		return HttpResponse("Oops! Looks like you input two invalid numbers, please imput real integers that are greater than 1") 

	# This query will search the database looking for 
	# image_width and image_height that are closest to 
	# the given parameters. I then filter for only public images
	# and order that result by the absolute differences as well
	# as the date the image was uploaded. I keep the result set
	# list to have only a length of one ( instead of using .first() ) 
	# so that I can pass the image nicely into html.

	image = User_Image.objects.annotate(
		abs_diff=Func(F('image_width') - img_width, 
		function='ABS')).annotate(
	    abs_diff=Func(F('image_height') - img_height, 
	    function='ABS')
	).filter(is_public=True).order_by('abs_diff', 'uploaded_at')[:1]

	if not image:

		# if the above query is null or empty, I would assume
		# that means the database is empty.

		return HttpResponse("No image with dimensions found")
	return render(request, 'images/specific_image.html', {'image': image})