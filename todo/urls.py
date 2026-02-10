from django.urls import path

from todo import views
urlpatterns = [
    path('addTsk/', views.addTask, name='addTask'),
      
]
