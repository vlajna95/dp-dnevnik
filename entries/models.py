from django.db import models
from django.utils import timezone

def _(text):
	return text


class Entry(models.Model):
	title = models.CharField(max_length=200, verbose_name=_("Naslov"))
	content = models.TextField(verbose_name=_("Sadržaj unosa"))
	date_created = models.DateTimeField(default=timezone.now, verbose_name=_("Datum pisanja"))

	class Meta:
		verbose_name = _("Unos")
		verbose_name_plural = _("Unosi")

	def __str__(self):
		return f"{self.date_created} {self.title}"
