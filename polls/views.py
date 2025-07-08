from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice


def index(request):
    """
    Display the latest 5 published questions.

    Retrieves the most recent questions ordered by publication date
    and renders them using the 'index.html' template.
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)


def detail(request, question_id):
    """
    Display a specific question and its choices.

    Retrieves the question by ID and renders the 'detail.html' template.
    If the question does not exist, returns a 404 error.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})


def results(request, question_id):
    """
    Display the results for a particular question.

    Retrieves the question by ID and renders the 'results.html' template,
    showing vote counts for each choice.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})


def vote(request, question_id):
    """
    Handle voting on a question.

    Processes the submitted vote from a POST request. If a choice is not
    selected or does not exist, it redisplays the voting form with an error.
    On success, it increments the selected choice's vote count and redirects
    to the results page.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
            pk=request.POST['choice']
        )
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form with an error message
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Prevent double posting on page refresh
        return HttpResponseRedirect(
            reverse('polls:results', args=(question_id,))
        )
