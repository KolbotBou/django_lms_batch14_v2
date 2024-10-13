from django.shortcuts import render

# Create your views here.

# When MAIN URL /library is accessed, index.html file will be viewed / shown
def index(request):
    return render(request, 'index.html')

# When about_us URL is accessed, about_us.html file will be viewed / shown
def about_us(request):
    return render(request, 'about_us.html')