from django import template

register = template.Library()

@register.simple_tag(name='get_photo_url', takes_context=False)
def get_photo_url(**kwargs):
    shoe = kwargs['shoe']
    if not shoe:
        return ''
    return str(shoe.get_photo_url())