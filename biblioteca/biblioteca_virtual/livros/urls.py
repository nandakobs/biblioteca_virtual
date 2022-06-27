from importlib.resources import path
from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('plataforma/', views.plataforma, name='plataforma'),
    path('logout/', views.logout_view, name='logout'),
]
