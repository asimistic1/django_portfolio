from django.db import models


class Bio(models.Model):
    name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    professional_description = models.TextField()

    class Meta:
        verbose_name_plural = 'bios'

    def __str__(self):
        return self.name
