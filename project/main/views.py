from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin)
from notifications.signals import notify
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Q
from django.forms.models import modelformset_factory
from django.views.generic import (
    TemplateView, DetailView, UpdateView,
    CreateView, DeleteView, ListView, RedirectView)

import markdown
from . import models, forms, mixins


class HomeView(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        projects = models.Project.objects \
            .prefetch_related('positions') \
            .all()
        project_needs = models.Position \
            .objects.order_by('name') \
            .distinct()

        context['projects'] = projects
        context['project_needs'] = project_needs

        return context


class FilterByPositionView(ListView):
    model = models.Project
    template_name = 'main/home.html'

    def get(self, request):
        search_position = request.GET.get('q', '')

        if search_position:
            projects = self.model.objects \
                .filter(positions__name=search_position)
        else:
            projects = self.model.objects.all()

        project_needs = models.Position.objects \
            .order_by('name').distinct()

        return render(request, self.template_name, {
            'projects': projects,
            'project_needs': project_needs,
            'search_position': search_position})


# -----
# Projects
# -----
class ProjectCreateView(
        PermissionRequiredMixin, LoginRequiredMixin,
        CreateView):

    model = models.Project
    form_project = forms.ProjectForm
    form_positions = forms.PositionFormSet
    permission_required = 'main.employer'

    template_name = 'main/project_create.html'

    def get(self, request):
        return render(request, self.template_name, {
            'form_project': self.form_project(prefix='project'),
            'form_positions': self.form_positions(prefix='positions')
        })

    def post(self, request, *args, **kwargs):
        form_project = self.form_project(request.POST, prefix='project')
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
            "form_positions": form_positions})


class ProjectDetailView(DetailView):
    model = models.Project
    template_name = 'main/project.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        project = models.Project.objects \
            .prefetch_related('positions') \
            .get(pk=self.kwargs.get('pk'))

        project.description = markdown.markdown(project.description)
        context['project'] = project

        return context


class ProjectEditView(
        PermissionRequiredMixin,
        LoginRequiredMixin,
        mixins.ProjectMustBeAuthorMixin,
        UpdateView):

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
        context['form_project'] = self.form_project(
            instance=project,
            prefix="project")
        context['form_positions'] = self.form_positions(
            instance=project,
            prefix="positions")

        return context

    def post(self, request, *args, **kwargs):
        project = self.model.objects.get(pk=self.kwargs.get('pk'))

        form_project = self.form_project(
            instance=project,
            data=request.POST,
            prefix='project')
        form_positions = self.form_positions(
            instance=project,
            data=request.POST,
            prefix="positions")

        if form_project.is_valid() and form_positions.is_valid():
            form_project.save()
            form_positions.save()

            return redirect('project', pk=project.pk)

        return render(request, self.template_name, {
            'project': project,
            'form_project': form_project,
            "form_positions": form_positions})


class ProjectDeleteView(
        LoginRequiredMixin, mixins.ProjectMustBeAuthorMixin,
        DeleteView):

    model = models.Project
    template_name = 'main/project_delete.html'
    success_url = reverse_lazy('home')


class ApplicationSubmitView(LoginRequiredMixin, CreateView):
    model = models.Application

    def get(self, request, *args, **kwargs):
        user = self.request.user
        project = get_object_or_404(
            models.Project,
            pk=self.kwargs.get('project_pk'))
        position = get_object_or_404(
            models.Position,
            pk=self.kwargs.get('position_pk'))
        profile = get_object_or_404(
            models.Profile,
            user=self.request.user)
        application = self.model.objects.filter(
            user=user,
            project=project,
            position=position)

        if not application:
            application = self.model.objects.create(
                user=user,
                profile=profile,
                position=position,
                project=project)

            messages.add_message(
                request,
                messages.SUCCESS,
                'Application has been submitted!',
                extra_tags='submission')

        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Application has already been submitted!',
                extra_tags='submission')

        return redirect(reverse('project', kwargs={
            'pk': self.kwargs.get('project_pk')}))


# -----
# Profile
# -----
class ProfileView(LoginRequiredMixin, TemplateView):
    model = models.Profile
    template_name = 'main/profile.html'

    def get(self, request, pk):
        try:
            profile = self.model.objects.get(pk=pk)
        except models.Profile.DoesNotExist:
            profile = self.model.objects.create(user=request.user)

        profile.short_bio = markdown.markdown(profile.short_bio)

        projects = models.Project.objects.filter(
            applications__profile__user=request.user,
            applications__status='Accepted')

        unread_notifications = request.user.notifications.unread()
        notifications = [str(x) for x in request.user.notifications.unread()]
        unread_notifications.mark_all_as_read()

        return render(request, self.template_name, {
            'notifications': notifications,
            'profile': profile,
            'projects': projects})


class ProfileEditView(
        LoginRequiredMixin, mixins.ProfileMustBeAuthorMixin,
        UpdateView):

    fields = ('name', 'short_bio', 'profile_image')
    model = models.Profile
    form_profile = forms.ProfileForm
    form_user_projects = forms.UserProjectFormSet
    form_skills = forms.SkillFormSet
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
        context['form_profile'] = self.form_profile(
            instance=profile,
            prefix="profile")
        context['form_user_projects'] = self.form_user_projects(
            instance=profile,
            prefix="user_projects")
        context['form_skills'] = self.form_skills(
            instance=profile,
            prefix="skills")

        return context

    def post(self, request, *args, **kwargs):
        profile = self.model.objects.get(user=request.user)
        projects = self.get_past_projects()

        form_profile = self.form_profile(
            request.POST, request.FILES,
            instance=profile,
            prefix='profile')
        form_user_projects = self.form_user_projects(
            instance=profile,
            data=request.POST,
            prefix="user_projects")
        form_skills = self.form_skills(
            instance=profile, data=request.POST,
            prefix="skills")

        if (form_profile.is_valid() and
                form_user_projects.is_valid() and
                form_skills.is_valid()):

            profile = form_profile.save()
            form_user_projects.save()
            form_skills.save()

            return redirect(reverse('profile', kwargs={
                'pk': profile.pk}))

        return render(request, self.template_name, {
            'form_profile': form_profile,
            "form_user_projects": form_user_projects,
            "form_skills": form_skills,
            "projects": projects})


# -----
# Applications
# -----
class ApplicationsView(
        PermissionRequiredMixin, LoginRequiredMixin,
        TemplateView):

    model = models.Application
    template_name = 'main/applications.html'
    permission_required = 'main.employer'

    def get(self, request):
        form_status = forms.ApplicationForm()
        redirect = ''

        filtered_applicants = self.model.objects \
            .filter(project__user=request.user)
        my_projects = models.Project.objects \
            .filter(user=request.user)
        my_proj_needs = models.Position.objects \
            .filter(Q(project__user=request.user)).distinct()

        return render(request, self.template_name, {
            'my_projects': my_projects,
            'my_proj_needs': my_proj_needs,
            'filtered_applicants': filtered_applicants,
            'form_status': form_status,
            'redirect': redirect})


class ApplicationsByProjectNeedView(
        PermissionRequiredMixin, LoginRequiredMixin,
        TemplateView):

    model = models.Application
    template_name = 'main/applications.html'
    permission_required = 'main.employer'

    def get(self, request):
        form_status = forms.ApplicationForm()
        redirect = 'proj_need'
        q = request.GET.get('q', '')

        if q:
            filtered_applicants = self.model.objects \
                .filter(Q(project__user=request.user) &
                        Q(position__name__iexact=q))
        else:
            filtered_applicants = self.model.objects \
                .filter(project__user=request.user)

        my_projects = models.Project.objects \
            .filter(user=request.user)
        my_proj_needs = models.Position.objects \
            .filter(Q(project__user=request.user)).distinct()

        return render(request, self.template_name, {
            'q': q,
            'my_projects': my_projects,
            'my_proj_needs': my_proj_needs,
            'filtered_applicants': filtered_applicants,
            'form_status': form_status,
            'redirect': redirect})


class ApplicationsByProjectView(
        PermissionRequiredMixin, LoginRequiredMixin,
        TemplateView):

    model = models.Application
    template_name = 'main/applications.html'
    permission_required = 'main.employer'

    def get(self, request):
        form_status = forms.ApplicationForm()
        redirect = 'project'
        q = request.GET.get('q', '')

        if q:
            filtered_applicants = self.model.objects \
                .filter(Q(project__title__iexact=q) &
                        Q(project__user=request.user))
        else:
            filtered_applicants = self.model.objects \
                .filter(project__user=request.user)

        my_projects = models.Project.objects \
            .filter(user=request.user)
        my_proj_needs = models.Position.objects \
            .filter(Q(project__user=request.user)) \
            .distinct()

        return render(request, self.template_name, {
            'q': q,
            'my_projects': my_projects,
            'my_proj_needs': my_proj_needs,
            'filtered_applicants': filtered_applicants,
            'form_status': form_status,
            'redirect': redirect})


class ApplicationsByStatusView(
        PermissionRequiredMixin, LoginRequiredMixin,
        TemplateView):

    model = models.Application
    template_name = 'main/applications.html'
    permission_required = 'main.employer'

    def get(self, request):
        form_status = forms.ApplicationForm()
        redirect = 'status'
        q = request.GET.get('q', '')

        if q:
            filtered_applicants = self.model.objects \
                .filter(Q(project__user=request.user) &
                        Q(status__iexact=q))
        else:
            filtered_applicants = self.model.objects \
                .filter(project__user=request.user)

        my_projects = models.Project.objects \
            .filter(user=request.user)
        my_proj_needs = models.Position.objects \
            .filter(Q(project__user=request.user)).distinct()

        return render(request, self.template_name, {
            'q': q,
            'my_projects': my_projects,
            'my_proj_needs': my_proj_needs,
            'filtered_applicants': filtered_applicants,
            'form_status': form_status,
            'redirect': redirect})


class ApplicantEditView(
        PermissionRequiredMixin, LoginRequiredMixin,
        mixins.ApplicationMustBeForAuthorMixin,
        UpdateView):

    model = models.Application
    template_name = 'main/applications.html'
    permission_required = 'main.employer'

    def post(self, request, *args, **kwargs):
        redirect_path = request.GET.get('redirect', '')
        q = request.GET.get('q', '')

        applicant = self.model.objects.get(pk=self.kwargs.get('pk'))
        applicant.status = request.POST['status']
        applicant.save()

        if applicant.status == 'Accepted':
            notify.send(
                request.user,
                recipient=applicant.user,
                verb=(
                    'Your application for position {} for project {} has been '
                    'accepted'.format(
                        applicant.position.name, applicant.project.title)))
        elif applicant.status == 'Rejected':
            notify.send(
                request.user,
                recipient=applicant.user,
                verb=(
                    'Your application for position {} for project {} has been '
                    'rejected'.format(
                        applicant.position.name, applicant.project.title)))

        if redirect:
            path = 'applications_' + redirect_path
        else:
            path = 'applications'

        if q:
            return redirect(reverse(path) + '?q=' + q)

        return redirect(reverse('applications'))


# -----
# Search
# -----
class SearchView(TemplateView):
    model = models.Project
    template_name = 'main/search.html'

    def get(self, request):
        search_term = request.GET.get('q', '')

        projects = self.model.objects \
            .prefetch_related('positions') \
            .filter(
                Q(title__icontains=search_term) |
                Q(description__icontains=search_term)) \
            .order_by('title')
        project_needs = models.Position.objects \
            .order_by('name').distinct()

        return render(request, self.template_name, {
            'projects': projects,
            'search_term': search_term,
            'project_needs': project_needs})