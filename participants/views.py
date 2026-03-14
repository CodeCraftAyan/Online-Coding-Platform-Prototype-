from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Participant
from contests.models import Contest


def join_contest(request, contest_id):

    contest = get_object_or_404(Contest, id=contest_id)

    now = timezone.now()

    # contest not started
    if now < contest.start_time:
        return render(request, "contest/not_started.html", {
            "contest": contest
        })

    # contest finished
    if now > contest.end_time:
        return render(request, "contest/contest_ended.html", {
            "contest": contest
        })

    # contest is running
    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']

        participant = Participant.objects.create(
            name=name,
            email=email,
            contest=contest
        )

        request.session['participant_id'] = participant.id

        return redirect("contest_dashboard", contest_id=contest.id)

    return render(request, "participants/join.html", {
        "contest": contest
    })
