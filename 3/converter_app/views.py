from django.shortcuts import render

# Create your views here.
def converter_view(request):
    return render(request, 'converter_app/converter.html', {})