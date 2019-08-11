from django.shortcuts import render

# Create your views here.



def login(request):
    return render(request, 'signin.html')

def logout(request):
    pass

def sign_up(request):
    return render(request, 'sign_up.html')