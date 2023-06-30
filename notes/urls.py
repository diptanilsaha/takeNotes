from django.urls import path
from .views import (
    NotesCreateView,
    NotesDeleteView,
    NotesListView,
    NotesLandingView,
    NotesDetailView
)

urlpatterns = [
    path('', NotesLandingView.as_view(), name='notes_landing'),
    path('notes/', NotesListView.as_view(), name='notes_list'),
    path('notes/add', NotesCreateView.as_view(), name='notes_create'),
    path('notes/<uuid:pk>', NotesDetailView.as_view(), name='notes_detail'),
    path('notes/<uuid:pk>/delete/', NotesDeleteView.as_view(), name='notes_delete')
]
