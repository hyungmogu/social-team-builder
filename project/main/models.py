from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey('auth.User')
    timeline = models.CharField(max_length=255)
    applicant_requirements = models.TextField()
    description = models.TextField()
    needs = models.ManyToManyField('Position', blank=True)

    def __str__(self):
        return self.title

class Position(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    related_skills = models.ManyToManyField('Skill', blank=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name