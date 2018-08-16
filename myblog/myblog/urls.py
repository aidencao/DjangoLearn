"""
Definition of urls for myblog.
"""

from django.conf.urls import url,include
from django.contrib import admin

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url(r'^blog/', include('blog.blog_urls')),
]
