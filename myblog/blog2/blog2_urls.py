from django.conf.urls import url

import blog2.views as bv2

urlpatterns = [
    url(r'^index/', bv2.index),  
]
