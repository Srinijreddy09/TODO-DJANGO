from django.urls import path

from todo import views
urlpatterns = [
    path('addTsk/', views.addTask, name='addTask'),
    path('markComplete/<int:task_id>/', views.markComplete, name='markComplete'),
    path('deleteTask/<int:task_id>/', views.deleteTask, name='deleteTask'),
    path('markUndone/<int:task_id>/', views.markUndone, name='markUndone'),
    path('editTask/<int:task_id>/', views.editTask, name='editTask'),
      
]
