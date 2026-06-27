from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = 'projects'

    def __str__(self):
        return self.title
