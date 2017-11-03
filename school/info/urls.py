from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^teacher/', views.teacher, name='teacher'),
    url(r'^course/', views.course, name='course'),
    url(r'^(?P<id>\d+)/$', views.id_course,name='disp'),
]