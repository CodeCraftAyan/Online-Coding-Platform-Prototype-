from django.db import models
from contests.models import Contest

class Participant(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()

    contest = models.ForeignKey(
        Contest,
        on_delete=models.CASCADE,
        related_name="participants"
    )

    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
