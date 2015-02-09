import urllib

from django import template
from ..forms import iCalendarForm

from ..utils import format_datetime


register = template.Library()



@register.simple_tag
def google_calendar(title, start_time='', end_time='', description='', address=''):
    params = urllib.urlencode({
        'action': 'TEMPLATE',
        'text': title.encode('utf-8'),
        'dates': '%s/%s' % (format_datetime(start_time), format_datetime(end_time)),
        'details': description.encode('utf-8'),
        'location': address.encode('utf-8'),
    })
    url = 'https://www.google.com/calendar/render?sprop=&sprop=name:&%s' % params

    return url


@register.inclusion_tag('calendartags/icalendar.html', takes_context=True)
def icalendar(context, title, start_time='', end_time='', description='', address=''):
    return {
        'form': iCalendarForm(initial={
            'title': title.encode('utf-8'),
            'start_time': start_time,
            'end_time': end_time,
            'description': description.encode('utf-8'),
            'address': address.encode('utf-8'),
            'url': context['request'].build_absolute_uri().encode('utf-8')
        }),
    }