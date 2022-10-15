from . import views
from django.urls import path


urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('blog/', views.post_list, name="post_list"),
    path('<slug:slug>/', views.post_detail, name="post_detail"),
    path('like<slug:slug>/', views.post_like, name="post_like"),
]