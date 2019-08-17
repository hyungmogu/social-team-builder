from django import forms
from django.forms.models import inlineformset_factory
from .models import Project, Position, Skill, Profile, UserProject

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

class ProfileForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Full Name', 'class': 'circle--input--h1'}))
    short_bio = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Tell us about yourself...'}))
    profile_image = forms.ImageField(widget=forms.FileInput)
    class Meta:
        fields = ('name', 'short_bio', 'profile_image')
        model = Profile

class SkillForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Skill'}))
    class Meta:
        fields = ('name',)
        model = Skill

class UserProjectForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name'}))
    url = forms.CharField(widget=forms.URLInput(attrs={'placeholder':'Url'}))
    class Meta:
        fields = ('name', 'url',)
        model = UserProject

PositionFormSet = inlineformset_factory(
    Project,
    Position,
    form=PositionForm,
    fields=('name','description',),
    extra=1,
    can_delete=True)


SkillFormSet = inlineformset_factory(
    Profile,
    Skill,
    form=SkillForm,
    fields=('name',),
    extra=1,
    can_delete=True)


UserProjectFormSet = inlineformset_factory(
    Profile,
    UserProject,
    form=UserProjectForm,
    fields=('name', 'url',),
    extra=1,
    can_delete=True)