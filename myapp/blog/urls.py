from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name="blogs"),
    path('<int:blog_id>/', views.description, name="description"),
]
