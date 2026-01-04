from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('view/', views.view, name='view'),
    path('add/', views.add, name='add'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
