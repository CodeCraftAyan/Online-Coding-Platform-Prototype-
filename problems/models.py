from django.db import models
from contests.models import Contest

class Problem(models.Model):

    contest = models.ForeignKey(
        Contest,
        on_delete=models.CASCADE,
        related_name="problems"
    )

    title = models.CharField(max_length=200)

    statement = models.TextField()

    time_limit = models.IntegerField(default=1)
    memory_limit = models.IntegerField(default=256)

    order = models.IntegerField()

    def __str__(self):
        return f"{self.contest.title} - {self.title}"


class TestCase(models.Model):

    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE,
        related_name="testcases"
    )

    input_data = models.TextField()
    expected_output = models.TextField()

    is_sample = models.BooleanField(default=False)
