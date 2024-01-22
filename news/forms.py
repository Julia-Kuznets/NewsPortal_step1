from django import forms
from django.core.exceptions import ValidationError

from .models import Post
class PostForm(forms.ModelForm):
    class Meta:
       model = Post
       fields = [
           'title',
           'text',
           'author'
       ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")

        if title == text:
            raise ValidationError(
                "Текст не должен быть идентичен названию."
            )

        return cleaned_data

class PostFormEdit(forms.ModelForm):
    class Meta:
       model = Post
       fields = [
           'title',
           'text',
           'author',
           'categoryType'
       ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")

        if title == text:
            raise ValidationError(
                "Текст не должен быть идентичен названию."
            )

        return cleaned_data