from django.urls import path

from . import views

urlpatterns = [
    path('good/<int:post_id>', views.good, name='good'),
    path('', views.index, name='index'),
]