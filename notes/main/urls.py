from django.urls import path, include
from .views import *
urlpatterns = [
    path("", Home.as_view()),
    path("notes/<int:id>", NoteView.as_view()),
    path('add_note', add_note),
    path("add_user", add_user)
    
]