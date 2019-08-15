from django import forms
from django.forms.models import inlineformset_factory
from .models import Project, Position, Skill

class ProjectForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Project Title', 'class': 'circle--input--h1'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Project description...'}))
    timeline = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Time estimate','class': 'circle--textarea--input'}))
    applicant_requirements = forms.CharField(widget=forms.Textarea(attrs={'class': 'circle--textarea--input'}))
    class Meta:
        exclude = ('user','needs',)
        model = Project

class PositionForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Position Title', 'class': 'circle--input--h3'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Position description...'}))
    related_skills = forms.ModelMultipleChoiceField(queryset=Skill.objects, required=False)
    class Meta:
        fields = ('name','description',)
        model = Position

PositionFormSet = inlineformset_factory(
    Project,
    Position,
    form=PositionForm,
    fields=('name','description',),
    extra=1)