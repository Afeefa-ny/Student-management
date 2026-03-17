from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
        path('list/', views.list, name='list'),

    path('view/', views.view, name='view'),
    path('add/', views.add, name='add'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
