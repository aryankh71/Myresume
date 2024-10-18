from django import template

register = template.Library()


@register.filter
def char_filter(value):
    return chr(value)


@register.filter
def type(value):
    return str(type(value))