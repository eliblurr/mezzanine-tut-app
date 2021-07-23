from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['author'].widget = forms.HiddenInput()