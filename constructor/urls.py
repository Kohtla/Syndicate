from django.conf.urls import url
from . import views

app_name = 'constructor'

urlpatterns = [
    # /shop/
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'^constructor/$',views.Constructor.as_view(), name = 'constructor'),

    url(r'^builder/$',views.Builder.as_view(), name = 'builder'),





]
