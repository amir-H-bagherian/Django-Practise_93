from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    if request.method == 'POST':
        return redirect(request.POST.get('op'))
    return render(request, 'calculator_app/home.html', {})

def addition_page(request):
    if request.method == 'POST':
        result = int(request.POST.get('num1')) + int(request.POST.get('num2'))
        context = {
            'op': '+',
            'result': result,
            'num1': request.POST.get('num1'),
            'num2': request.POST.get('num2')
        }
        return render(request, 'calculator_app/calc.html', context)
    return render(request, 'calculator_app/calc.html', {})  
 
def multiplication_page(request):
    if request.method == 'POST':
        result = int(request.POST.get('num1')) * int(request.POST.get('num2'))
        context = {
            'op': '*',
            'result': result,
            'num1': request.POST.get('num1'),
            'num2': request.POST.get('num2')
        }
        return render(request, 'calculator_app/calc.html', context)
    return render(request, 'calculator_app/calc.html', {})  
 
def division_page(request):
    if request.method == 'POST':
        result = int(request.POST.get('num1')) / int(request.POST.get('num2'))
        context = {
            'op': '/',
            'result': result,
            'num1': request.POST.get('num1'),
            'num2': request.POST.get('num2')
        }
        return render(request, 'calculator_app/calc.html', context)
    return render(request, 'calculator_app/calc.html', {})  
 
def subtraction_page(request):
    if request.method == 'POST':
        result = int(request.POST.get('num1')) - int(request.POST.get('num2'))
        context = {
            'op': '-',
            'result': result,
            'num1': request.POST.get('num1'),
            'num2': request.POST.get('num2')
        }
        return render(request, 'calculator_app/calc.html', context)
    return render(request, 'calculator_app/calc.html', {})  