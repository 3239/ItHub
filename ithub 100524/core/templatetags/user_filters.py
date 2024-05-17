import datetime

from django import template
from django.conf import settings
from django.utils.timesince import timesince

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})
@register.filter(name='without_placeholder')
def without_placeholder(field):
    """
    """
    field.field.widget.attrs['placeholder']=' '
    return field
@register.filter(name='add_placeholder')
def add_placeholder(field,value):
    """
    """
    field.field.widget.attrs['placeholder']=value
    return field
@register.filter(name='add_attr')
def add_attr(field,value):
    """
    """
    field.field.widget.attrs[value]=None
    return field
