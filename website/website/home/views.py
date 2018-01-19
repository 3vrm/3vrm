from django.shortcuts import render

# Create your views here.
def base(request):
	return render(request, "home/base.html")

def homepage(request):
	return render(request, 'home/homepage.html')

def services(request):
	return render(request, 'home/services.html')