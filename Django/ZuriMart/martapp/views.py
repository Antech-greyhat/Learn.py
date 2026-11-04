from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'martapp/about.html')
def contacts(request):
    return render(request, 'martapp/contact.html')
def index(request):
    return render(request, 'martapp/index.html')
def services(request):
    return render(request, 'martapp/services.html')
def subscribe(request):
    return render(request, 'martapp/subscribe.html')