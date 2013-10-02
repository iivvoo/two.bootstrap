from django import template

register = template.Library()

@register.filter(name='fieldtype')
def fieldtype(field, expected):
    try:
        t = field.field.widget.__class__.__name__
        return t.lower() == expected
    except AttributeError:
        pass
    return False

@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class":css})
