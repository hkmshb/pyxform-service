from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'xlsformPost', 'xlsform_main.views.consume_xlsform', name='xlsform-post'),
    # Examples:
    # url(r'^$', 'pyxform_service.views.home', name='home'),
    # url(r'^pyxform_service/', include('pyxform_service.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
