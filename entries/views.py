from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Entry


class LockedView(LoginRequiredMixin):
	login_url = "admin:login"


class EntryListView(LockedView, ListView):
	model = Entry
	queryset = Entry.objects.all().order_by("-date_created")


class EntryDetailView(LockedView, DetailView):
	model = Entry


class EntryCreateView(LockedView, SuccessMessageMixin, CreateView):
	model = Entry
	fields = ["title", "content", "date_created"]
	success_url = reverse_lazy("entry_list")
	success_message = "Unos je uspešno dodat."


class EntryUpdateView(LockedView, SuccessMessageMixin, UpdateView):
	model = Entry
	fields = ["title", "content", "date_created"]
	success_message = "Unos je uspešno izmenjen."

	def get_success_url(self):
		return reverse_lazy("entry_detail", kwargs={"pk": self.object.id})


class EntryDeleteView(LockedView, DeleteView):
	model = Entry
	success_url = reverse_lazy("entry_list")
	success_message = "Unos je uspešno uklonjen."

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super().delete(request, *args, **kwargs)
