from django.conf.urls import url

from eventex.subscriptions.views import detail, new


urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^i(\d+)/$', detail, name='detail'),
]
