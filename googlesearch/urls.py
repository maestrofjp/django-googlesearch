import django
from django.views.generic.base import TemplateView

version = django.get_version()

if version < 1.6:
    from django.conf.urls.defaults import patterns, url
else:
    from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',

    url(
        r'^results/$',
        TemplateView.as_view(template_name='googlesearch/results.html')
        name='googlesearch-results'
    ),

    url(
        r'^cref-cse\.xml/$', 
        'googlesearch.views.cref_cse', 
        {},
        name='googlesearch-cref-cse'
    ),
)
