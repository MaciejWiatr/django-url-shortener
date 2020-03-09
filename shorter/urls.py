from django.urls import path
from . import views

urlpatterns = [
    path('<code>/', views.link_redir, name='link_redir'),
    path('', views.index, name='index')
]
app_name = 'shorter'
