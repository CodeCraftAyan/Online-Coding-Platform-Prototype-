from django.shortcuts import render, get_object_or_404
from .models import Problem


def problem_detail(request, problem_id):

    problem = get_object_or_404(Problem, id=problem_id)

    testcases = problem.testcases.filter(is_sample=True)

    return render(request, "problems/problem_detail.html", {
        "problem": problem,
        "testcases": testcases
    })
