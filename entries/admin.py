from django.contrib import admin
from .models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
	list_display = ["title", "date_created"]
	list_filter = ["date_created"]
	search_fields = ["title", "content"]
