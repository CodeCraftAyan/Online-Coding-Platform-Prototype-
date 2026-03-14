from django.shortcuts import render
from .models import Contest
from django.utils import timezone
from submissions.models import Submission


def contest_list(request):

    contests = Contest.objects.all().order_by("-start_time")

    return render(request, "contest/contest_list.html", {
        "contests": contests,
        "now": timezone.now()
    })

def contest_dashboard(request, contest_id):

    contest = Contest.objects.get(id=contest_id)

    problems = contest.problems.all().order_by("order")

    return render(request, "contest/dashboard.html", {
        "contest": contest,
        "problems": problems
    })


def scoreboard(request, contest_id):

    contest = Contest.objects.get(id=contest_id)

    participants = contest.participants.all()

    scoreboard = []

    for p in participants:

        solved = Submission.objects.filter(
            participant=p,
            verdict="Accepted"
        ).values("problem").distinct().count()

        scoreboard.append({
            "name": p.name,
            "solved": solved
        })

    scoreboard.sort(key=lambda x: -x["solved"])

    return render(request, "contest/scoreboard.html", {
        "scoreboard": scoreboard
    })
