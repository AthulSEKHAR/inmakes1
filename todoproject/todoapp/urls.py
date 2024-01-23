from .import views
from django.urls import path
app_name='todoapp'


urlpatterns = [
    path('',views.add,name='add'),
    path('detail/', views.detail, name='detail'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:taskid>/', views.update, name='update'),
    path('cbvhome/', views.Tasklistview.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.TaskDetailview.as_view(), name='cbvdetail'),
    path('cbvedit/<int:pk>/', views.TaskUpdateview.as_view(), name='cbvedit'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteview.as_view(), name='cbvdelete'),

    ]