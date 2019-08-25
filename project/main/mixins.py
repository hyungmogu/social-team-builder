from . import models
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse


class ProjectMustBeAuthorMixin:
    def dispatch(self, request, *args, **kwargs):
        project = get_object_or_404(
            models.Project,
            pk=self.kwargs.get('pk'))

        if request.user.pk != project.user.pk:
            return redirect(reverse('project', kwargs={
                'pk': project.pk}))

        return super().dispatch(request, *args, **kwargs)


class ProfileMustBeAuthorMixin:
    def dispatch(self, request, *args, **kwargs):
        profile = get_object_or_404(
            models.Profile,
            pk=self.kwargs.get('pk'))

        if request.user.pk != profile.user.pk:
            return redirect(reverse('profile', kwargs={
                'pk': profile.pk}))

        return super().dispatch(request, *args, **kwargs)


class ApplicationMustBeForAuthorMixin:
    def dispatch(self, request, *args, **kwargs):
        application = get_object_or_404(
            models.Application,
            pk=self.kwargs.get('pk'))

        if request.user.pk != application.project.user.pk:
            return redirect(reverse('applications'))

        return super().dispatch(request, *args, **kwargs)