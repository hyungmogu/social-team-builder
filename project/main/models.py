from django.db import models
from django.conf import settings

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    timeline = models.CharField(max_length=255)
    applicant_requirements = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    projects = models.ForeignKey(Project)
    short_bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images', null=True, blank=True)
    skills = models.TextField()

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey('Project', related_name="positions")
    description = models.TextField()
    related_skills = models.ManyToManyField('Skill', blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


