from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.forms.models import modelformset_factory
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

        projects = models.Project.objects.prefetch_related('positions').all()
        project_needs = models.Position.objects.order_by('name').distinct()

        context['projects'] = projects
        context['project_needs'] = project_needs

        return context

class ProjectDetailView(DetailView):
    model = models.Project
    template_name = 'main/project.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        project = models.Project.objects.prefetch_related('positions').get(pk=self.kwargs.get('pk'))
        context['project'] = project

        return context

class ProjectEditView(UpdateView):
    fields = (
        'title', 'needs', 'timeline',
        'applicant_requirements', 'description')
    model = models.Project
    template_name = 'main/project_edit.html'

class ProjectCreateView(CreateView):
    model = models.Project
    form_project = forms.ProjectForm
    form_positions = forms.PositionFormSet

    template_name = 'main/project_create.html'

    def get(self, request):
        return render(request, self.template_name, {
            'form_project': self.form_project(prefix='project'),
            'form_positions':self.form_positions(prefix='positions')
        })

    def post(self, request, *args, **kwargs):
        """Creates Project on save"""
        form_project = self.form_project(request.POST,prefix='project')
        form_positions = self.form_positions(request.POST, prefix="positions")

        if form_project.is_valid() and form_positions.is_valid():
            project = form_project.save(commit=False)
            project.user = request.user
            project.save()

            positions = form_positions.save(commit=False)

            for position in positions:
                position.project = project
                position.save()

            return redirect('project', pk=project.pk)

        return render(request, self.template_name, {
            'form_project': form_project,
            "form_positions": form_positions
        })


class ProjectDeleteView(DeleteView):
    model = models.Project
    success_url = reverse_lazy('home')

def profile(request):
    return render(request, 'main/profile.html')

def profile_edit(request):
    return render(request, 'main/profile_edit.html')

def search(request):
    return render(request, 'main/search.html')

def applications(request, pk):
    return render(request, 'main/applications.html')
