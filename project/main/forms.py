from django import forms
from django.forms.models import modelformset_factory
from .models import Project, Position, Skill

class ProjectForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Project Title', 'class': 'circle--input--h1'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Project description...'}))
    timeline = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Time estimate','class': 'circle--textarea--input'}))
    applicant_requirements = forms.CharField(widget=forms.Textarea(attrs={'class': 'circle--textarea--input'}))
    needs = forms.ModelMultipleChoiceField(queryset=Position.objects, required=False)
    class Meta:
        fields = ('title','description', 'timeline', 'applicant_requirements',)
        model = Project

class PositionForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Position Title', 'class': 'circle--input--h3'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Position description...'}))
    related_skills = forms.ModelMultipleChoiceField(queryset=Skill.objects, required=False)
    class Meta:
        fields = ('name','description',)
        model = Position

PositionFormSet = modelformset_factory(
    Position,
    fields=('name','description',)
)