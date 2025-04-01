from django.urls import path
from .views import (
    HomePage,
    TagPage,
    TaskCreate,
    TaskUpdate,
    TaskDelete,
    TagCreate,
    TagUpdate,
    TagDelete,
    ToggleTaskStatusView,
)

app_name = "manager"

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("create-task/", TaskCreate.as_view(), name="task-create"),
    path("update-task/<int:pk>/", TaskUpdate.as_view(), name="task-update"),
    path("delete-task/<int:pk>/", TaskDelete.as_view(), name="task-delete"),
    path("tags/", TagPage.as_view(), name="tags"),
    path("create-tag/", TagCreate.as_view(), name="tag-create"),
    path("update-tag/<int:pk>/", TagUpdate.as_view(), name="tag-update"),
    path("delete-tag/<int:pk>/", TagDelete.as_view(), name="tag-delete"),
    path("task/<int:pk>/toggle", ToggleTaskStatusView.as_view(), name="toggle-task-status"),
]