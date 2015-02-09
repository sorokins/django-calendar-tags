from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    'calendartags.views',
    url('^ical/$', 'icalendar', name='calendartags_icalendar')

)