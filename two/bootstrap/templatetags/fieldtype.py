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
    attrs = {}
    try:
        orig_class = dict(field.field.widget.attrs).get('class', "")
    except AttributeError:
        orig_class = ""
    attrs['class'] = "%s %s" % (orig_class, css)

    return field.as_widget(attrs=attrs)
