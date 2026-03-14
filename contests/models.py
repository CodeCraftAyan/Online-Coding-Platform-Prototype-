from django.db import models

class Contest(models.Model):

    title = models.CharField(max_length=200)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    duration = models.IntegerField(help_text="minutes")

    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
