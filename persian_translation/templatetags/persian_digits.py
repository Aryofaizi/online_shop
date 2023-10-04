from django import template

register = template.Library()


@register.filter
def to_persian_digits(value):
    value = str(value)
    trans_table = value.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")
    return value.translate(trans_table)
