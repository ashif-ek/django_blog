from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    # path('<int:id>/', views.blog_details, name='blog_details'),
    path('<int:id>/', views.blog_details, name='blog_details'),

    path('create/', views.create_post, name='create_post'),
    path('edit/<int:id>/', views.edit_post, name='edit_post'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
]