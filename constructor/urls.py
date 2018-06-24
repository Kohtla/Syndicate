from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'constructor'

urlpatterns = [
    # /shop/
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'^constructor/$',views.Constructor.as_view(), name = 'constructor'),

    url(r'^builder/$',views.Builder.as_view(), name = 'builder'),
    url(r'report/$', views.Report.as_view(), name = 'report'),
    url(r'report/(?P<pk>[0-9]+)/$',views.Generator.as_view(), name = 'generator'),
]


