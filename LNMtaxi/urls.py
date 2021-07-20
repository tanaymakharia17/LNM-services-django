from django.urls import path
from . import views

urlpatterns = [
    path('', views.LNMtaxi_home, name='LNMtaxi_home'),
    path('view_blogs', views.view_blogs, name='view_blogs'),
    path('insert_blogs/', views.insert_blogs, name='insert_blogs'),
    path('delete_blog/<int:id>', views.delete_blog, name= 'delete_blog')
]