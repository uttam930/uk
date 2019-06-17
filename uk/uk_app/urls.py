from django.conf.urls import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
    url(r'^storage-list?$', 'asgard_app.views.storge_list'),
    url(r'^pre_migrate?$', 'asgard_app.views.pre_migrate_list'),
    url(r'migrate?$', 'asgard_app.views.migrate_list')
)

urlpatterns = format_suffix_patterns(urlpatterns)


