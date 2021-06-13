from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Category, Notebook, CartProduct, Cart, Customer

User = get_user_model()


class ShopTestCases(TestCase):

    def setUP(self) -> None:
        self.user = User.objects.create(username='testuser', password='password')
        self.category = Category.objects.create(name='Nešiojamieji kompiuteriai', slug='notebooks')
