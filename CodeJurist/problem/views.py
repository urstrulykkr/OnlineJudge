from multiprocessing import Process

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db import connection
from CodeJurist.settings import BASE_URL

from user.models import Submission
from problem.constants import Judge

from .judges import judge_gcc, judge_gpp, judge_python
from .models import Problem, TestCase


@login_required(login_url='login_n')
def problem(request, prob_id):
    problem = Problem.objects.get(id=prob_id)

    if request.method == 'POST':
        submission = Submission(user=request.user,
                                problem=problem,
                                code=request.POST['code'],
                                judge=request.POST['language'])
        testcases = list(submission.problem.testcase_set.all())
        print(submission.judge)
        submission.save()
        p = Process(target=run_testcases, args=(submission, testcases))
        p.start()
        return redirect('submissions')

    context = {
        'problem': problem,
        'samples': TestCase.objects.filter(problem_id=problem.id, is_sample=True),
        'judges': Submission.JUDGE_CHOICES,
        'BASE_URL': BASE_URL,
    }
    return render(request, 'problem.html', context)


def run_testcases(sub: Submission, testcases):
    if sub.judge == Judge.PY2:
        output = judge_python(sub, testcases, False)
    elif sub.judge == Judge.PY3:
        output = judge_python(sub, testcases, True)
    elif sub.judge == Judge.GCC:
        output = judge_gcc(sub, testcases)
    elif sub.judge == Judge.GPP14:
        output = judge_gpp(sub, testcases, 14)
    elif sub.judge == Judge.GPP17:
        output = judge_gpp(sub, testcases, 17)
    elif sub.judge == Judge.GPP20:
        output = judge_gpp(sub, testcases, 20)

    sub.verdict = output['verdict']
    sub.time = output['time']
    connection.close()
    sub.save()