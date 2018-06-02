from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static
from shop import views as v

urlpatterns = [
    url(r'^$', include('main.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^shop/', include('shop.urls')),
    url(r'^forum/', include('forum.urls')),
    url(r'^constructor/', include('constructor.urls')),
    #url(r'^shop/constructor', v.ConstructorView.as_view(), name = "constructor")

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)
