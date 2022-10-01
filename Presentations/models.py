from django.db import models
from django.urls import reverse

# Create your models here.


class Presentation(models.Model):
    title = models.CharField(max_length=240, null=True)
    author = models.CharField(max_length=120, null=True)
    date = models.DateField(null=True)
    file_uploads = models.JSONField(null=True)

    def get_absolute_url(self):
        return reverse("Blog:blog_article", kwargs={"id": self.id})
