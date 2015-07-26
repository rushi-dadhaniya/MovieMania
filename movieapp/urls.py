from django.conf.urls import url
from movieapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^movies/$', views.movie_list),
    url(r'^movies/(?P<pk>[0-9]+)/$', views.movie_details),
]

urlpatterns = format_suffix_patterns(urlpatterns)
