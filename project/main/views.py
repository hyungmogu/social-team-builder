from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse

from . import models, forms
# Create your views here.


# Temporary. Will be replaced with serializer once developed.
def home(request):
    projects = models.Project.objects.all()
    project_needs = models.Project.objects.order_by('needs').values('needs__name').distinct()

    return render(request, 'main/home.html', {
        'projects': projects,
        'project_needs': project_needs
    })

def project(request, pk):
    project = get_object_or_404(models.Project, pk=pk)

    return render(request, 'main/project.html', {
        "project": project
    })

def project_edit(request, pk):
    project = get_object_or_404(models.Project, pk=pk)

    return render(request, 'main/project_edit.html', {
        'project': project
    })

def project_create(request):
    return render(request, 'main/project_create.html')

def project_delete(request, pk):
    """Removes a project from model"""
    try:
        obj = models.Project.objects.get(pk=pk)
        obj.delete()
    finally:
        return redirect(reverse('home'))

def profile(request, pk):
    return render(request, 'main/profile.html')

def profile_edit(request, pk):
    return render(request, 'main/profile_edit.html')

def search(request):
    return render(request, 'main/search.html')

def applications(request, pk):
    return render(request, 'main/applications.html')
