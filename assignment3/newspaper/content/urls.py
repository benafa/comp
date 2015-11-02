from django.conf.urls import url


from content.views import index, detail


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<article_id>[0-9]+)/$', detail, name='detail')
   # url(r'^tinymce/', include('tinymce.urls')),

]