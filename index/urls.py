from django.conf.urls import url

from index.views import index

# app_name='index'
urlpatterns = [
    url(r'^$', index, name='index'),
]
