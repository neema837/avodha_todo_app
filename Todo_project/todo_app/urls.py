from django.urls import path
from . import views

urlpatterns = [

    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('', views.task_view, name='task_view'),
    path('update/<int:id>/', views.update, name='update'),
    path('vtask', views.TaskListView.as_view(), name='vtask'),
    path('vdetail/<int:pk>/', views.TaskDetailView.as_view(), name='vdetail'),
    path('vupdate/<int:pk>/', views.TaskUpdateview.as_view(), name='vupdate'),
    path('vdelete/<int:pk>/', views.TaskDeleteview.as_view(), name='vdelete'),

]
