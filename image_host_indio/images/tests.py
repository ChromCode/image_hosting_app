import datetime

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.utils import timezone

from .models import User_Image

# Create your tests here.

# Tests for model properties

def test_image_width(self):
	test = SimpleUploadedFile("file.jpg", "file_content", content_type="image/jpeg")
