from abc import ABC
from django.shortcuts import render
from my_app.forms import AboutForm
from my_app.models import About
# Create your views here.
def index(request):
    if request.method == 'POST':
        data_form = AboutForm(data = request.POST)
        if data_form.is_valid():
            first_name = data_form.cleaned_data['first_name']
            last_name = data_form.cleaned_data['last_name']
            email = data_form.cleaned_data['email']
            message = data_form.cleaned_data['message']
            allow_mailing = data_form.cleaned_data['allow_mailing']
            about_object = About(first_name = first_name, last_name = last_name,
            email = email, message = message, allow_mailing = allow_mailing)
            about_object.save()
            print('Saved')

    form = AboutForm()
    about_data = About.objects.all()
    return render(request, "index.html", {'form':form, 'data': about_data})





