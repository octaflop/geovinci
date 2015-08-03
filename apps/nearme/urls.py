from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'views.front.index', name='index'),
]
