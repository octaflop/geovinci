from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'nearme.views.front.index', name='index'),
]
