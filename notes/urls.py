from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.list_note_create, name="list_note_create"),
    path("notes/<int:pk>/", views.note_details, name="note_details"),
]
