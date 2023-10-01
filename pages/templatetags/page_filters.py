from django import template
register = template.Library()


@register.filter
def to_uppercase(value):
    return f"{value.upper()}"
