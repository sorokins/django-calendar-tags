import logging
from django.http import HttpResponse
from .utils import format_datetime
from .forms import iCalendarForm

logger = logging.getLogger(__name__)

def icalendar(request):
    form = iCalendarForm(request.POST)
    if form.is_valid():
        content = '\n'.join([
            'BEGIN:VCALENDAR',
            'VERSION:2.0',
            'BEGIN:VEVENT',
            'URL:' + form.cleaned_data['url'],
            'DTSTART:' + format_datetime(form.cleaned_data['start_time']),
            'DTEND:' + format_datetime(form.cleaned_data['end_time']),
            'SUMMARY:' + form.cleaned_data['title'],
            'DESCRIPTION:' + form.cleaned_data['description'],
            'LOCATION:' + form.cleaned_data['address'],
            'END:VEVENT',
            'END:VCALENDAR'
        ])

        response = HttpResponse(content, content_type='text/calendar')
        response['Content-Disposition'] = 'attachment; filename="ical.ics"'
        return response
    else:
        logger.debug(form.errors)
        return HttpResponse('error')
