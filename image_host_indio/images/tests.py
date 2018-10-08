import datetime
import tempfile

from PIL import Image

from django.test import override_settings
from django.test import TestCase
from django.utils import timezone

from .models import User_Image
from .forms import ImageForm

def get_temporary_image(temp_file):
    size = (200, 200)
    color = (255, 0, 0, 0)
    image = Image.new("RGB", size, color)
    image.save(temp_file, 'jpeg')
    return temp_file

# Tests for creating model properties

class UserImageModelTests(TestCase):

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_create_image_test(self):
        temp_file = tempfile.NamedTemporaryFile()
        test_image = get_temporary_image(temp_file)
        image = User_Image.objects.create(image=test_image.name)
        self.assertEqual(len(User_Image.objects.all()), 1)

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_create_isPublic_true_test(self):
        temp_file = tempfile.NamedTemporaryFile()
        test_image = get_temporary_image(temp_file)
        image = User_Image.objects.create(image=test_image.name, is_public=True)
        test_query = User_Image.objects.first()
        self.assertIs(test_query.is_public, True)

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_create_isPublic_false_test(self):
        temp_file = tempfile.NamedTemporaryFile()
        test_image = get_temporary_image(temp_file)
        image = User_Image.objects.create(image=test_image.name, is_public=False)
        test_query = User_Image.objects.first()
        self.assertIs(test_query.is_public, False)

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_create_image_width_test(self):

        """ The temporary image created has a width of 200, so we will
        test if the image has the correct width dimension """

        temp_file = tempfile.NamedTemporaryFile()
        test_image = get_temporary_image(temp_file)
        image = User_Image.objects.create(image=test_image.name,)
        test_query = User_Image.objects.first()
        self.assertEqual(test_query.image.width, 200)

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_create_image_height_test(self):

    	""" The temporary image created has a height of 200, so we will
    	test if the image has the correct height dimension """

    	temp_file = tempfile.NamedTemporaryFile()
    	test_image = get_temporary_image(temp_file)
    	image = User_Image.objects.create(image=test_image.name,)
    	test_query = User_Image.objects.first()
    	self.assertEqual(test_query.image.height, 200)
		
