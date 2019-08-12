from django.shortcuts import render


from . import models
# Create your views here.


# Temporary. Will be replaced with serializer once developed.
def home(request):
    projects = models.Project.objects.all()
    project_needs = models.Project.objects.order_by('needs').values('needs__name').distinct()

    return render(request, 'main/home.html', {
        'projects': projects,
        'project_needs': project_needs
    })

def profile(request, user_pk):
    return render(request, 'main/profile.html')

def profile_edit(request, user_pk):
    return render(request, 'main/profile_edit.html')

def project(request, project_pk):
    return render(request, 'main/project.html')

def project_edit(request, project_pk):
    return render(request, 'main/project_edit.html')

def project_create(request):
    return render(request, 'main/project_create.html')

def search(request):
    return render(request, 'main/search.html')

def applications(request):
    return render(request, 'main/applications.html')
