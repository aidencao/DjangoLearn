from django.conf.urls import url

import blog.views as bv

urlpatterns = [
    url(r'^index/', bv.index),
    url(r'^article/(?P<article_id>[0-9]+)', bv.article_page),
]