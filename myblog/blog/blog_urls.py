from django.conf.urls import url

import blog.views as bv

urlpatterns = [
    url(r'^index/', bv.index),  
]