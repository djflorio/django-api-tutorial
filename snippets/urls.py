from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]

# This allows us to specify a format (such as .json) at the
# end of the URL. For example, localhost:8000/snippets/1.json
urlpatterns = format_suffix_patterns(urlpatterns)