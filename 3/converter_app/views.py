from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def converter_view(request):
    return render(request, 'converter_app/converter.html', {})

def create_result(request):
    if request.method == 'POST':
        text = request.POST.get('html-text')
        return HttpResponse(text)
    else:
        return redirect('home')