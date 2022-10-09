from . import views
from django.urls import path


urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('blog/', views.post_list, name="post_list"),
]