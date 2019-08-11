from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey('auth.User')
    needs = models.ManyToManyField('Position')
    timeline = models.CharField(max_length=255)
    applicant_requirements = models.CharField(max_length=255)
    description = models.TextField()


class Position(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    related_skills = models.ManyToManyField('Skill')


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)