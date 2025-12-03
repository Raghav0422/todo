from django.urls import path
from tasks import views

urlpatterns = [
    path('tasks/', views.index),
    path('update_task/<str:pk>',views.updatetask, name='update_task'), # name is used in url tag in list.html
]