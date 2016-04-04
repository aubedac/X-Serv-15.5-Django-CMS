from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^insert/(.*)/(.*)$', "cms.views.insert"),
    url(r'^pages/$', "cms.views.showPages"),
    url(r'^(\d+)$', "cms.views.page"),
    url(r'^admin/', "include(admin.site.urls)"),
    url(r'.*', "cms.views.notFound")
)
