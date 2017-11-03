from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^display/', views.disp),
    url(r'^product/', views.product,name='list'),
    url(r'^(?P<id>\d+)/$', views.id_product,name='product'),
    url(r'^order/', views.order_list),
    url(r'^(?P<id>\d+)/edit/$', views.post_update,name='update'),
    url(r'^(?P<id>\d+)/delete/$', views.post_delete),
    #url(r'^view/', views.my_view),
   url(r'^temp/', views.temp),
]
