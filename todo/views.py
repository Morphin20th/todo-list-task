from django.views import generic

from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
