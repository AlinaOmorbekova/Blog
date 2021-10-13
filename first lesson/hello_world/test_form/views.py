from django.shortcuts import render
from test_form.forms import MyForm
# Create your views here.
def form_url(request):
    form = MyForm()
    return render(request, "test-form.html", {'abc':form})
