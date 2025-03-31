from asyncio import TaskGroup

from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

from manager.models import Task, Tag
from manager.forms import TaskForm


class HomePage(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags").order_by("is_done", "-datetime")
    context_object_name = "tasks"
    template_name = "home/index.html"


class TagPage(generic.ListView):
    model = Tag
    queryset = Tag.objects.all()
    context_object_name = "tags"
    template_name = "home/tags.html"


class TaskCreate(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:home")
    template_name = "home/task_form.html"


class TaskUpdate(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "home/task_form.html"
    success_url = reverse_lazy("manager:home")


class TaskDelete(generic.DeleteView):
    model = Task
    template_name = "home/task_confirm_delete.html"
    success_url = reverse_lazy("manager:home")


class TagCreate(generic.CreateView):
    model = Tag
    fields = ["name", ]
    success_url = reverse_lazy("manager:tags")
    template_name = "home/tag_form.html"


class TagUpdate(generic.UpdateView):
    model = Tag
    fields = ["name", ]
    template_name = "home/tag_form.html"
    success_url = reverse_lazy("manager:tags")


class TagDelete(generic.DeleteView):
    model = Tag
    template_name = "home/tag_confirm_delete.html"
    success_url = reverse_lazy("manager:tags")


def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("manager:home")