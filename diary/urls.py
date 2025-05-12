from django.urls import path

from diary.apps import DiaryConfig

from .views import EntryCreateView, EntryDeleteView, EntryDetailView, EntryUpdateView, HomeView, IndexView

app_name = DiaryConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("entries/", IndexView.as_view(), name="index"),
    path("create/", EntryCreateView.as_view(), name="create_entry"),
    path("edit/<int:pk>/", EntryUpdateView.as_view(), name="edit_entry"),
    path("entry/<int:pk>/", EntryDetailView.as_view(), name="entry_detail"),
    path("entry/delete/<int:pk>/", EntryDeleteView.as_view(), name="delete_entry"),
]
