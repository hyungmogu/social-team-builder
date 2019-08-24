from . import models
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

class MustBeProjectAuthorMixin:
    def get(self, request, *args, **kwargs):
        project = models.Project.objects.get(pk=self.kwargs.get('pk'))

        if request.user.pk != project.user.pk:
            return redirect(reverse('project', kwargs={
                'pk': project.pk
            }))

        return super().get(request, *args, **kwargs)


class MustBeProfileAuthorMixin:
    def get(self, request, *args, **kwargs):
        profile = models.Profile.objects.get(pk=self.kwargs.get('pk'))

        if request.user.pk != profile.user.pk:
            return redirect(reverse('profile', kwargs={
                'pk': profile.pk
            }))

        return super().get(request, *args, **kwargs)