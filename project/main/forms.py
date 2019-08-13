from django import forms

from .models import Project, Position


class ProjectForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Project Title', 'class': 'circle--input--h1'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Project description...'}))
    timeline = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Time estimate','class': 'circle--textarea--input'}))
    applicant_requirements = forms.CharField(widget=forms.Textarea(attrs={'class': 'circle--textarea--input'}))
    needs = forms.ModelMultipleChoiceField(queryset=Position.objects, required=False)

    class Meta:
        exclude = ('user','needs',)
        model = Project


class PositionForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Position Title', 'class': 'circle--input--h3'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Position description...'}))
    class Meta:
        model = Position
        exclude = ('related_skills',)