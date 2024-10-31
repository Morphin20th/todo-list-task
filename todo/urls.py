from django.urls import path

from todo.views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TagCreateView,
    TagUpdateView,
    TaskUpdateView,
    TaskDeleteView,
    TagDeleteView,
    toggle_task_done,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("task-create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/toggle-done/", toggle_task_done, name="toggle-task-done"),
]

app_name = "todo"
