from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Q
from django.forms.models import modelformset_factory
from django.views.generic import (
    TemplateView, DetailView, UpdateView,
    CreateView, DeleteView, ListView, RedirectView)

from . import models, forms, mixins


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


class ProjectEditView(
        PermissionRequiredMixin,
        LoginRequiredMixin,
        mixins.MustBeProjectAuthorMixin,
        UpdateView
    ):
    fields = (
        'title', 'timeline',
        'applicant_requirements', 'description')
    model = models.Project
    form_project = forms.ProjectForm
    form_positions = forms.PositionFormSet
    template_name = 'main/project_edit.html'
    permission_required = 'main.employer'

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


class ProjectCreateView(LoginRequiredMixin, CreateView):
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


class ProjectDeleteView(
        LoginRequiredMixin,
        mixins.MustBeProjectAuthorMixin,
        DeleteView
    ):
    model = models.Project
    template_name= 'main/project_delete.html'
    success_url = reverse_lazy('home')


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


class ProfileView(LoginRequiredMixin, TemplateView):
    model = models.Profile
    template_name = 'main/profile.html'

    def get(self, request, pk):
        try:
            profile = self.model.objects.get(pk=pk)
        except models.Profile.DoesNotExist:
            profile = self.model.objects.create(user=request.user)

        projects = models.Project.objects.filter(
            applications__profile__user=request.user,
            applications__status='Accepted')

        return render(request, self.template_name, {
            'profile': profile,
            'projects': projects
        })


class ProfileEditView(
        LoginRequiredMixin,
        mixins.MustBeProfileAuthorMixin,
        UpdateView
    ):

    fields = ('name', 'short_bio', 'profile_image')
    model = models.Profile
    form_profile = forms.ProfileForm
    form_user_projects = forms.UserProjectFormSet
    form_skills =  forms.SkillFormSet
    template_name = 'main/profile_edit.html'

    def get_past_projects(self):
        projects = models.Project.objects.filter(
            applications__profile__user=self.request.user,
            applications__status='Accepted')

        return projects

    def get_object(self):
        obj = get_object_or_404(self.model, user=self.request.user)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile = self.model.objects.get(user=self.request.user)
        projects = self.get_past_projects()

        context['projects'] = projects
        context['form_profile'] = self.form_profile(instance=profile, prefix="profile")
        context['form_user_projects'] = self.form_user_projects(instance=profile, prefix="user_projects")
        context['form_skills'] = self.form_skills(instance=profile, prefix="skills")

        return context

    def post(self, request, *args, **kwargs):
        """Creates Project on save"""
        profile = self.model.objects.get(user=request.user)
        projects = self.get_past_projects()

        form_profile = self.form_profile(request.POST, request.FILES, instance=profile, prefix='profile')
        form_user_projects = self.form_user_projects(instance=profile, data=request.POST, prefix="user_projects")
        form_skills = self.form_skills(instance=profile, data=request.POST, prefix="skills")

        if form_profile.is_valid() and form_user_projects.is_valid() and form_skills.is_valid():
            profile = form_profile.save()
            form_user_projects.save()
            form_skills.save()

            return redirect(reverse('profile', kwargs={
                'pk': profile.pk
            }))

        return render(request, self.template_name, {
            'form_profile': form_profile,
            "form_user_projects": form_user_projects,
            "form_skills": form_skills,
            "projects": projects
        })


class ApplicationSubmitView(LoginRequiredMixin, CreateView):
    model = models.Application

    def get(self, request, *args, **kwargs):
        # 1. fetch project position and user
        user = self.request.user
        project = get_object_or_404(models.Project, pk=self.kwargs.get('project_pk'))
        position = get_object_or_404(models.Position, pk=self.kwargs.get('position_pk'))
        profile= get_object_or_404(models.Profile, user=self.request.user)

        # 2. try to fetch application. if application exists, then raise error message
        application = self.model.objects.filter(user=user,project=project,position=position)

        # 3. if application does not exist, then create an application, set it to pending, and
        if not application:
            application = self.model.objects.create(
                user=user,
                profile=profile,
                position=position,
                project=project
            )

            messages.add_message(request, messages.SUCCESS, 'Application has been submitted!')
        else:
            # 3. if application exists, then add error message
            messages.add_message(request, messages.ERROR, 'Application has already been submitted!')

        return redirect(reverse('project', kwargs={
            'pk': self.kwargs.get('project_pk')
        }))


class ApplicationsView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    model = models.Application
    template_name = 'main/applications.html'
    permission_required = 'main.employer'

    def get(self, request):
        form_status = forms.ApplicationForm()
        redirect = ''

        # 1. get all types of queries
        filtered_applicants = self.model.objects.filter(project__user=request.user)

        my_projects = models.Project.objects.filter(user=request.user)
        my_proj_needs = models.Position.objects.filter(Q(project__user=request.user)).distinct()
        return render(request, self.template_name, {
            'my_projects': my_projects,
            'my_proj_needs': my_proj_needs,
            'filtered_applicants': filtered_applicants,
            'form_status': form_status,
            'redirect': redirect
        })


class ApplicationsByProjectNeedView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    model = models.Application
    template_name = 'main/applications.html'
    permission_required = 'main.employer'

    def get(self, request):
        form_status = forms.ApplicationForm()
        redirect = 'proj_need'

        # 1. get all types of queries
        q = request.GET.get('q', '')

        if q:
            filtered_applicants = self.model.objects.filter(Q(project__user=request.user)&Q(position__name__iexact=q))
        else:
            filtered_applicants = self.model.objects.filter(project__user=request.user)

        my_projects = models.Project.objects.filter(user=request.user)
        my_proj_needs = models.Position.objects.filter(Q(project__user=request.user)).distinct()
        return render(request, self.template_name, {
            'q': q,
            'my_projects': my_projects,
            'my_proj_needs': my_proj_needs,
            'filtered_applicants': filtered_applicants,
            'form_status': form_status,
            'redirect': redirect
        })


class ApplicationsByProjectView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    model = models.Application
    template_name = 'main/applications.html'
    permission_required = 'main.employer'

    def get(self, request):
        form_status = forms.ApplicationForm()
        redirect='project'

        # 1. get all types of queries
        q = request.GET.get('q', '')

        if q:
            filtered_applicants = self.model.objects.filter(Q(project__title__iexact=q)&Q(project__user=request.user))
        else:
            filtered_applicants = self.model.objects.filter(project__user=request.user)

        my_projects = models.Project.objects.filter(user=request.user)
        my_proj_needs = models.Position.objects.filter(Q(project__user=request.user)).distinct()
        return render(request, self.template_name, {
            'q': q,
            'my_projects': my_projects,
            'my_proj_needs': my_proj_needs,
            'filtered_applicants': filtered_applicants,
            'form_status': form_status,
            'redirect': redirect
        })


class ApplicationsByStatusView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    model = models.Application
    template_name = 'main/applications.html'
    permission_required = 'main.employer'

    def get(self, request):
        form_status = forms.ApplicationForm()
        redirect='status'

        # 1. get all types of queries
        q = request.GET.get('q', '')

        if q:
            filtered_applicants = self.model.objects.filter(Q(project__user=request.user)&Q(status__iexact=q))
        else:
            filtered_applicants = self.model.objects.filter(project__user=request.user)

        my_projects = models.Project.objects.filter(user=request.user)
        my_proj_needs = models.Position.objects.filter(Q(project__user=request.user)).distinct()
        return render(request, self.template_name, {
            'q': q,
            'my_projects': my_projects,
            'my_proj_needs': my_proj_needs,
            'filtered_applicants': filtered_applicants,
            'form_status': form_status,
            'redirect': redirect
        })


class ApplicantEditView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = models.Application
    template_name = 'main/applications.html'
    permission_required = 'main.employer'

    def post(self, request, *args, **kwargs):
        redirect_path = request.GET.get('redirect','')
        q = request.GET.get('q','')

        # 1. Get applicant
        applicant = self.model.objects.get(pk=self.kwargs.get('pk'))
        applicant.status = request.POST['status']

        applicant.save()
        messages.add_message(request, messages.INFO, "Application status has been changed successfully")

        if redirect:
            path = 'applications_' + redirect_path
        else:
            path = 'applications'

        # 4. redirect user back to appication page
        if q:
            return redirect(reverse(path) + '?q=' + q)
        return redirect(reverse('applications'))
