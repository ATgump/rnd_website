from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class CalendarEvent(models.Model):
    date = models.DateField()
    event_name = models.CharField(max_length=120, null=True)
    event_creator = models.CharField(max_length=120, null=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.event_name

    def get_absolute_url(self):
        return reverse("CalendarApp:single-event-view",
                       kwargs={"somestringnamehere": self.event_name})
