from django.urls import path

from todo.views import TaskListView, TagListView, TaskCreateView, TagCreateView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("task-create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
]

app_name = "todo"