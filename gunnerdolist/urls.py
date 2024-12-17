from . import views
from django.urls import path

urlpatterns = [
      path('', views.HomeView.as_view(), name="home"),
      path('taskpage/', views.task_details, name='tasks'),
      path('update_task/<str:pk>/', views.update_task, name='update_task'),
      path('delete_task/<str:pk>/', views.delete_task, name='delete_task')
]