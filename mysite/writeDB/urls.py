rom django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /writeDB/
    url(r'^$', views.index, name='index'),
	]
