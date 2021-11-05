from django import template

register = template.Library()

@register.filter
def index(sequence, position):
    position = int(position.split('-')[1])
    return sequence[position]