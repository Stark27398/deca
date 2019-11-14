from django import template
from users.models import contentId
register = template.Library()
@register.filter(name='first')
def first(value):
    name = contentId.objects.get(typeId=value)
    return name.classtype[0]
