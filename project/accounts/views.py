from django.shortcuts import render

# Create your views here.



def login(request):
    return render(request, 'accounts/signin.html')

def logout(request):
    pass

def sign_up(request):
    return render(request, 'accounts/signup.html')