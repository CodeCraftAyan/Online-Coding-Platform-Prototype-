from django.shortcuts import redirect, render, get_object_or_404
from .models import Submission
from problems.models import Problem
from .judge import judge_submission
from .models import SubmissionTestCase


def submit_code(request, problem_id):

    participant_id = request.session.get("participant_id")

    code = request.POST['code']
    lang = request.POST['language']

    problem = Problem.objects.get(id=problem_id)

    submission = Submission.objects.create(
        participant_id=participant_id,
        problem=problem,
        code=code,
        language=lang
    )

    judge_submission(submission)

    return redirect("submission_detail", submission.id)


def submission_detail(request, submission_id):

    submission = get_object_or_404(Submission, id=submission_id)

    testcases = SubmissionTestCase.objects.filter(submission=submission)

    return render(request, "submissions/submission_detail.html", {
        "submission": submission,
        "testcases": testcases
    })
