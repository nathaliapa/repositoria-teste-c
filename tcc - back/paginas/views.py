from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'paginas/home.html')

def paginas(request):
    return render(request, 'paginas/paginas.html')