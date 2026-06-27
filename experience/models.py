from django.db import models


class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'experience'
        ordering = ['-start_date']

    def __str__(self):
        return self.title
