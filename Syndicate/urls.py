from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from shop import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^shop/', include('shop.urls')),
    url(r'^forum/', include('forum.urls')),

]

urlpatterns = format_suffix_patterns(urlpatterns)
