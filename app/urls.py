from django.urls import path,include
from . import views
urlpatterns = [

  path('', views.landing, name='landing'),
  path('login/',views. login_view, name="login"),
   path('register/', views.register_view, name='register'),
  path('admin-dashboard/', views.admin_dashboard, name="admin_dashboard"),
  path('logout/', views.logout_view, name='logout'),
]