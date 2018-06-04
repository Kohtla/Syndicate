from django.conf.urls import url
from . import views

app_name = 'forum'

urlpatterns = [
    # /shop/
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    # /shop/
    url(r'^register/$', views.UserFormView.as_view(), name = 'register'),
    # /shop/3
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = "detail"),
    # /shop/theme/add/*
    url(r'theme/add/$', views.ThemeCreate.as_view(), name = 'theme-add'),

    url(r'^logout/$', views.Log_out.as_view(), name = 'logout'),

    url(r'^login/$', views.Log_in.as_view(), name='login'),

    url(r'^login/$', views.ProfileDetailView.as_view(),name = 'profile')



]
