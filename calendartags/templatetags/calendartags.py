from datetime import datetime
import urllib

from django import template
from ..forms import iCalendarForm

from ..utils import format_datetime, format_datetime_yahoo, format_duration_yahoo


register = template.Library()



@register.simple_tag
def google_calendar(title, start_time='', end_time='', description='', address=''):
    params = {
        'action': 'TEMPLATE',
        'text': title.encode('utf-8'),
        'details': description.encode('utf-8') if description is not None else '',
        'location': address.encode('utf-8') if address is not None else '',
    }
    if isinstance(start_time, datetime) and isinstance(end_time, datetime):
        params.update({
            'dates': '%s/%s' % (format_datetime(start_time), format_datetime(end_time)),

        })
    params = urllib.urlencode(params)
    url = 'https://www.google.com/calendar/render?sprop=&sprop=name:&%s' % params

    return url


@register.simple_tag
def yahoo_calendar(title, start_time='', end_time='', description='', address=''):

    duration = None

    if end_time:
        duration = end_time - start_time

    params = urllib.urlencode({
        'title': title.encode('utf-8'),
        'in_loc': address.encode('utf-8'),
        'desc': description.encode('utf-8'),
        'st': format_datetime_yahoo(start_time),
        'dur': format_duration_yahoo(duration),
    })

    url = 'http://calendar.yahoo.com/?v=60&view=d&type=20&%s' % params

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