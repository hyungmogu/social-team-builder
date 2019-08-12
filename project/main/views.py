from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.forms import formset_factory
from django.views.generic import (
    TemplateView, DetailView, UpdateView,
    CreateView, DeleteView)

from . import models, forms
# Create your views here.


# Temporary. Will be replaced with class based views once developed.
class HomeView(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        projects = models.Project.objects.all()
        project_needs = models.Project.objects.order_by('needs').values('needs__name').distinct()

        context['projects'] = projects
        context['project_needs'] = project_needs

        return context

class ProjectDetailView(DetailView):
    model = models.Project
    template_name = 'main/project.html'

class ProjectEditView(UpdateView):
    fields = (
        'title', 'needs', 'timeline',
        'applicant_requirements', 'description')
    model = models.Project
    template_name = 'main/project_edit.html'

class ProjectCreateView(CreateView):
    model = models.Project
    form_project = forms.ProjectForm
    form_positions = formset_factory(forms.PositionForm)

    template_name = 'main/project_create.html'

    def get(self, request):
        return render(request, self.template_name, {
            'form_project': self.form_project,
            "form_positions":self.form_positions
        })

class ProjectDeleteView(DeleteView):
    model = models.Project
    success_url = reverse_lazy('home')

def profile(request, pk):
    return render(request, 'main/profile.html')

def profile_edit(request, pk):
    return render(request, 'main/profile_edit.html')

def search(request):
    return render(request, 'main/search.html')

def applications(request, pk):
    return render(request, 'main/applications.html')
