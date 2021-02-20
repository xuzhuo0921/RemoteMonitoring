from django.conf.urls import url
from django.urls import path


from . import views

# urlpatterns = [
#     url(r'^monitor/$', views.index, name='index'),
# ]

urlpatterns = [
    url(r'monitor/$',views.index,name='index'),
    url(r'^monitor/(?P<pIndex>[0-99]+)$', views.index, name='index'),
    url(r'^monitor/add$', views.add, name='monitor_add'),
    url(r'^monitor/insert$', views.insert, name='monitor_insert'),
    url(r'^monitor/details/(?P<hid>[0-99]+)$', views.details, name='monitor_details'),
    url(r'^monitor/edit/(?P<hid>[0-99]+)$', views.edit, name='monitor_edit'),
    url(r'^monitor/delete/(?P<hid>[0-99]+)$', views.delete, name='monitor_delete'),
    url(r'^monitor/update/(?P<hid>[0-99]+)$', views.update, name='monitor_update'),
    url(r'^getHostStat/(?P<ipaddr>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$', views.get_host_stat, name='getHostStat'),



#     path('monitor/', views.index,name='index'),
#     path('monitor/index.html', views.index,name='index'),
#     path('monitor/add', views.add,name='monitor_add'),
#     url(r'^monitor/(?P<pIndex>[0-99]+)$', views.index, name='index'),
]
