from . import models
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse

class ProjectMustBeAuthorMixin:
    def get(self, request, *args, **kwargs):
        project = models.Project.objects.get(pk=self.kwargs.get('pk'))

        if request.user.pk != project.user.pk:
            return redirect(reverse('project', kwargs={
                'pk': project.pk
            }))

        return super().get(request, *args, **kwargs)


class ProfileMustBeAuthorMixin:
    def get(self, request, *args, **kwargs):
        profile = models.Profile.objects.get(pk=self.kwargs.get('pk'))

        if request.user.pk != profile.user.pk:
            return redirect(reverse('profile', kwargs={
                'pk': profile.pk
            }))

        return super().get(request, *args, **kwargs)


class ApplicationMustBeForAuthorMixin:
    def dispatch(self, request, *args, **kwargs):
        application = get_object_or_404(models.Application, pk=self.kwargs.get('pk'))

        if request.user.pk != application.project.user.pk:
            return redirect(reverse('applications'))

        return super().dispatch(request, *args, **kwargs)