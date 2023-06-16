from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == 'POST':
        print(request.POST.get('op'))
    
    return render(request, 'calculator_app/home.html', {})
