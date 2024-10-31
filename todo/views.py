from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskForm
from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"

    def get_queryset(self):
        return Task.objects.order_by("done", "-created_at").prefetch_related("tags")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("todo:tag-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


def toggle_task_done(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.done = not task.done
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo:task-list"))
