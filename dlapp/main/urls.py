from django.conf.urls import url

from . import views

from main.views import Home, upload

#urlpatterns = [url(r'^$', views.index, name='index')]
urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^upload/$', upload, name='upload'),
]
