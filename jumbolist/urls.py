from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'jlist.views.load_home', name='home'),
    url(r'^signup/$', 'jlist.views.register', name='register'),
    url(r'^login/$', 'jlist.views.login_attempt', name='login_attempt'),
    url(r'^profile/$', 'jlist.views.profile', name='profile'),
    url(r'^sell/$', 'jlist.views.sellers_page', name='sellers'),
    url(r'^additem/$', 'jlist.views.additem', name='add'),
    url(r'^manage/$', 'jlist.views.manage', name='manage'),
    url(r'^marketplace/$', 'jlist.views.display_items', name='display_items'),
   # url(r'^saveditems/$', 'jlist.views.display_watched_items', name='display_watched_items'),
    url(r'^saveditems/$', 'jlist.views.display_saved_items', name='display_saved_items'),

    url(r'^buy/$', 'jlist.views.buyers_page', name='buyers'),
    url(r'^marketplace/filter_attempt/$', 'jlist.views.filter_attempt', name='filter_attempt'),

    url(r'^marketplace/item/(?P<item_id>\w+)$', 'jlist.views.item_page', name='item'),
    url(r'^manage/item/(?P<item_id>\w+)$', 'jlist.views.item_page', name='seller_item'),
    url(r'^save/item/(?P<item_id>\w+)$', 'jlist.views.save_item', name='save_item'),
    url(r'^watch/item/(?P<item_id>\w+)$', 'jlist.views.watched_item', name='save_item'),
    url(r'^remove/item/(?P<item_id>\w+)$', 'jlist.views.remove_item', name='remove'),
    url(r'^offer/(?P<item_id>\w+)$', 'jlist.views.send_email', name='remove'),







    # url(r'^jumbolist/', include('jumbolist.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
