from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('LNMshop/', include('LNMshop.urls'), name='LNMshop'),
    path('LNMtaxi/', include('LNMtaxi.urls'), name='LNMtaxi'),
    path('forgotPassword/', views.forgotPassword, name='forgot_password'),
    path('logout/', views.logout, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),


]
