from django.conf.urls import patterns, include, url
from django.contrib import admin

v1_urls = patterns(
    '',
)

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/auth/', include(
        'rest_framework.urls',
        namespace='rest_framework')),
    url(r'^api/v1/', include(v1_urls, namespace='v1'))
)
