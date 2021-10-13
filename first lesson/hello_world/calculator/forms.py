from django import forms

class MyCalcForm(forms.Form):
    first_num = forms.IntegerField()
    second_num = forms.IntegerField()
    operation = forms.CharField()
    