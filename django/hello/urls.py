from django.urls import include, path,  re_path

from . import plotly_dash

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^home/$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    re_path(r'^about/$', views.AboutPageView.as_view(), name='about'),
    ]