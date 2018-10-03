from django import forms
from images.models import User_Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = User_Image
        fields = ('is_public', 'image', )