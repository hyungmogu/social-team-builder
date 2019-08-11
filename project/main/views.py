from django.shortcuts import render

# Create your views here.


# Temporary. Will be replaced with serializer once developed.
def home(request):
    return render(request, 'main/home.html')

def profile(request, user_pk):
    return render(request, 'main/profile.html')

def profile_edit(request, user_pk):
    return render(request, 'main/profile_edit.html')

def project(request, project_pk):
    return render(request, 'main/project.html')

def project_edit(request, project_pk):
    return render(request, 'main/project_edit.html')

def project_create(request, project_pk):
    return render(request, 'main/project_create.html')

def search(request):
    return render(request, 'main/search.html')

def applications(request):
    return render(request, 'main/applications.html')
