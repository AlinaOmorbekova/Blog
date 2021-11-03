from django.shortcuts import render
from calculator.forms import MyCalcForm
# Create your views here.
# Create your views here.
def calc_form_url(request):
    answer = 0
    if request.method == "POST":
        print('Ответ:')
        data = MyCalcForm(request.POST)
        if data.is_valid():
            if data.cleaned_data['operation'] == '+':
                answer = data.cleaned_data['first_num'] + data.cleaned_data['second_num']
                print(answer)
            elif data.cleaned_data['operation'] == '-':
                answer = data.cleaned_data['first_num'] - data.cleaned_data['second_num']
                print(answer) 
            elif data.cleaned_data['operation'] == '*':
                answer = data.cleaned_data['first_num'] * data.cleaned_data['second_num']
                print(answer)  
            elif data.cleaned_data['operation'] == '/':
                answer = data.cleaned_data['first_num'] / data.cleaned_data['second_num']
                print(answer)         
    form = MyCalcForm()
    return render(request, "calculator.html", {'calc':form})