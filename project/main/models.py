from django.db import models
from django.conf import settings

# Create your models here.

class Application(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    profile = models.ForeignKey('Profile', related_name="applications")
    project = models.ForeignKey('Project', related_name="applications")
    position = models.ForeignKey('Position', related_name="applications")

    def __str__(self):
        return "[{}] - {} {}".format(profile, project, position)

class Project(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    timeline = models.CharField(max_length=255)
    applicant_requirements = models.TextField()
    description = models.TextField()
    # end_date = models.DateField()

    def __str__(self):
        return self.title

class UserProject(models.Model):
    name= models.CharField(max_length=255)
    url = models.URLField()
    profile = models.ForeignKey('Profile', related_name="user_projects")


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
    name = models.CharField(max_length=255)
    short_bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images', null=True, blank=True)

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
    profile = models.ForeignKey('Profile', related_name="skills")

    def __str__(self):
        return self.name


