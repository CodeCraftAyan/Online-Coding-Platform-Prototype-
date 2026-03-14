from django.db import models
from participants.models import Participant
from problems.models import Problem

class Submission(models.Model):

    participant = models.ForeignKey(
        Participant,
        on_delete=models.CASCADE
    )

    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE
    )

    code = models.TextField()

    language = models.CharField(
        max_length=20,
        choices=[
            ("py", "Python"),
            ("cpp", "C++"),
            ("java", "Java")
        ]
    )

    verdict = models.CharField(
        max_length=50,
        default="Pending"
    )

    time = models.FloatField(null=True, blank=True)
    memory = models.IntegerField(null=True, blank=True)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.participant} - {self.problem}"


class SubmissionTestCase(models.Model):

    submission = models.ForeignKey(
        Submission,
        on_delete=models.CASCADE
    )

    testcase_number = models.IntegerField()

    status = models.CharField(max_length=50)

    time = models.FloatField(null=True)
