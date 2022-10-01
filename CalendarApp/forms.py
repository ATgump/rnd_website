from django import forms

from .models import CalendarEvent


class CalendarEventForm(forms.ModelForm):
    class Meta:
        model = CalendarEvent
        fields = [
            "date",
            "event_name",
            "event_creator",
        ]
