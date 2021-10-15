from django.urls import path
from . import views

urlpatterns = [
	path("", views.EntryListView.as_view(), name="entry_list"),
	path("unos/<int:pk>", views.EntryDetailView.as_view(), name="entry_detail"),
	path("dodaj/", views.EntryCreateView.as_view(), name="entry_create"),
	path("unos/<int:pk>/izmeni", views.EntryUpdateView.as_view(), name="entry_update"),
	path("unos/<int:pk>/ukloni", views.EntryDeleteView.as_view(), name="entry_delete"),
]