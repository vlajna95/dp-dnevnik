from django.apps import AppConfig

def _(text):
	return text


class EntriesConfig(AppConfig):
	default_auto_field = "django.db.models.BigAutoField"
	name = "entries"
	verbose_name = _("Unosi")
