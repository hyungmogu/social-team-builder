from django import template

register = template.Library()

@register.filter
def add_class(field, class_name):
    """
    Referenced from the site
    https://stackoverflow.com/questions/4124220/django-adding-css-classes-when-rendering-form-fields-in-a-template
    """
    return field.as_widget(attrs={
        "class": " ".join((field.css_classes(), class_name))
    })