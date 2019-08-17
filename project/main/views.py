from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Q
from django.forms.models import modelformset_factory
from django.views.generic import (
    TemplateView, DetailView, UpdateView,
    CreateView, DeleteView, ListView)

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
        'title', 'timeline',
        'applicant_requirements', 'description')
    model = models.Project
    form_project = forms.ProjectForm
    form_positions = forms.PositionFormSet
    template_name = 'main/project_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        project = models.Project.objects.get(pk=self.kwargs.get('pk'))
        positions = models.Position.objects.filter(project=project)

        context['project'] = project
        context['form_project'] = self.form_project(instance=project, prefix="project")
        context['form_positions'] = self.form_positions(instance=project, prefix="positions")

        return context

    def post(self, request, *args, **kwargs):
        """Creates Project on save"""
        project = self.model.objects.get(pk=self.kwargs.get('pk'))

        form_project = self.form_project(instance=project, data=request.POST, prefix='project')
        form_positions = self.form_positions(instance=project, data=request.POST, prefix="positions")

        if form_project.is_valid() and form_positions.is_valid():
            form_project.save()
            form_positions.save()

            return redirect('project', pk=project.pk)

        return render(request, self.template_name, {
            'project': project,
            'form_project': form_project,
            "form_positions": form_positions
        })

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
    template_name= 'main/project_delete.html'
    success_url = reverse_lazy('home')

def profile(request):
    return render(request, 'main/profile.html')

def profile_edit(request):
    return render(request, 'main/profile_edit.html')

def search(request):
    return render(request, 'main/search.html')

class SearchView(TemplateView):
    model = models.Project
    template_name = 'main/search.html'

    def get(self, request):
        # 1. fetch query params
        search_term = request.GET.get('q', '')

        # 2. filter projects based by title or description
        projects = self.model.objects.prefetch_related('positions').filter(Q(title__icontains=search_term)|Q(description__icontains=search_term)).order_by('title')
        project_needs = models.Position.objects.order_by('name').distinct()

        # 3. return results on view
        return render(request, self.template_name, {
            'projects': projects,
            'search_term': search_term,
            'project_needs': project_needs
        })

class SearchByPositionView(ListView):
    model = models.Project
    template_name = 'main/home.html'

    def get(self, request):
        # 1. fetch query params
        position = request.GET.get('q', '')

        # 2. filter projects by position
        projects = self.model.objects.filter(positions__name=position)
        project_needs = models.Position.objects.order_by('name').distinct()

        # 3. display result on search / home page
        return render(request, self.template_name, {
            'projects': projects,
            'project_needs': project_needs,
            'search_position': position
        })


class ProfileView(TemplateView):
    model = models.Profile
    template_name = 'main/profile.html'

    def get(self, request):

        profile = get_object_or_404(self.model, user=request.user)

        return render(request, self.template_name, {
            'profile': profile
        })

def applications(request, pk):
    return render(request, 'main/applications.html')
