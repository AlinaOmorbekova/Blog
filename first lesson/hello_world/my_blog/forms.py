from django import forms
from django.db import models
from django.forms.fields import CharField
from my_blog.models import CreateArticle

class SendMesgForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    message = forms.CharField(max_length=200)
    allow_mailing = forms.BooleanField()

class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = CreateArticle
        exclude = ('created_data', 'updated_data')