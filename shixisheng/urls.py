from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shixisheng.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'shixisheng.views.home'),
    url(r'^index$', 'shixisheng.views.home'),
    url(r'^theme$', 'shixisheng.views.theme'),
    url(r'^indextwo$', 'shixisheng.views.indextw'),
    url(r'^item$', 'shixisheng.views.item'),
    url(r'^flow$', 'shixisheng.views.liucheng'),

    url(r'^goodstudent$', 'shixisheng.views.goodstudent'),


    url(r'^company$', 'shixisheng.views.companys'),
    url(r'^comone$', 'shixisheng.views.comone'),
    url(r'^comsec$', 'shixisheng.views.comsec'),
    url(r'^comthree$', 'shixisheng.views.comthr'),

    url(r'^student$', 'shixisheng.views.students'),
    url(r'^daoshi$', 'shixisheng.views.daoshi'),

    url(r'^zhuce$', 'shixisheng.views.register'),

    


    url(r'^lc.html$', 'shixisheng.views.lc'),
    url(r'^fd.html$', 'shixisheng.views.fd'),
    url(r'^time$', 'shixisheng.views.time'),
    url(r'^upload$', 'shixisheng.views.upload'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
 	{'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
    url(r'^admin/', include(admin.site.urls)),
)
