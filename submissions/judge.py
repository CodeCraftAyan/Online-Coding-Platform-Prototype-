import subprocess
import tempfile
import time

from .models import SubmissionTestCase


def normalize_output(text):
    return "\n".join(line.strip() for line in text.strip().splitlines())


def judge_submission(submission):

    testcases = submission.problem.testcases.all()

    # create temp file once
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as f:
        f.write(submission.code.encode())
        filename = f.name

    verdict = "Accepted"
    max_time = 0

    for i, tc in enumerate(testcases, start=1):

        start = time.time()

        result = subprocess.run(
            ["python", filename],
            input=tc.input_data,
            text=True,
            capture_output=True
        )

        end = time.time()

        exec_time = end - start
        max_time = max(max_time, exec_time)

        output = normalize_output(result.stdout)
        expected = normalize_output(tc.expected_output)

        if output == expected:
            status = "AC"
        else:
            status = "WA"
            verdict = "Wrong Answer"

        # SAVE testcase result
        SubmissionTestCase.objects.create(
            submission=submission,
            testcase_number=i,
            status=status,
            time=exec_time
        )

        if status != "AC":
            break

    submission.verdict = verdict
    submission.time = max_time
    submission.save()
