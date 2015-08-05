from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'nearme.views.front.index', name='index'),
    url(r'^coarse$', 'nearme.views.api.coarse', name='coarse'),
    url(r'^fine$', 'nearme.views.api.fine', name='fine'),
]
