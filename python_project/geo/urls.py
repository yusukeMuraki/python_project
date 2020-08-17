from django.urls import path

from . import views

app_name = 'geo'
urlpatterns = [
    path('geo/', views.index, name='index'),
    path('geo/plot/<str:pid>', views.get_svg, name='plot'),
    path('geo/prefecture/<int:pid>', views.prefecture, name='prefecture'),
    path('geo/set_prefecture', views.set_prefecture, name='set_prefecture')
]