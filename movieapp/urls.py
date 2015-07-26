from django.conf.urls import url
from movieapp import views

urlpatterns = [
    url(r'^movies/$', views.movie_list),
    url(r'^movies/(?P<pk>[0-9]+)/$', views.movie_details),
]
