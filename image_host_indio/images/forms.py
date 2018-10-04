# Code obtained and modified from: 
# https://github.com/sibtc/simple-file-upload
# Original Author: https://github.com/sibtc

from django import forms
from images.models import User_Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = User_Image
        fields = ('is_public', 'image', )