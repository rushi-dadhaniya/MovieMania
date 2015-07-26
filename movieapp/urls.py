from django.conf.urls import url
from movieapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^movies/$', views.MovieList.as_view()),
    url(r'^movies/(?P<pk>[0-9]+)/$', views.MoviewDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
