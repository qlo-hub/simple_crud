from django.db.models import fields
from django.forms import ModelForm
from .models import *


class BooksForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorsForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
