from django import forms

class MyCalcForm(forms.Form):
    first_num = forms.FloatField()
    second_num = forms.FloatField()
    operation = forms.CharField()
    
