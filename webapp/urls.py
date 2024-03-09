from django.urls import path
from webapp.views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView

urlpatterns = [
    path('', TaskListView.as_view(), name='index'),
    path('create_task/', TaskCreateView.as_view(), name='create_task'),
    path('edit_task/<int:pk>/', TaskUpdateView.as_view(), name='edit_task'),
    path('delete_task/<int:pk>/', TaskDeleteView.as_view(), name='delete_task'),
    path('detail_task/<int:pk>/', TaskDetailView.as_view(), name='detail_task')
]
