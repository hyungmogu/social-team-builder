from django.shortcuts import render

# Create your views here.


# Temporary. Will be replaced with serializer once developed.
def home(request):
    return render(request, 'main/home.html')