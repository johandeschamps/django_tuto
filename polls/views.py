from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
               :5
               ]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

def polls_list(request):
    polls = Question.objects.all()
    return render(request, 'polls/all.html', {'polls': polls})


def frequency(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.get_choices()
    total_votes = sum(choice.votes for choice in choices)

    for choice in choices:

        if total_votes > 0:
            choice.percentage = (choice.votes / total_votes) * 100
        else:
            choice.percentage = 0

    context = {
        'question': question,
        'choices': choices,
        'total_votes': total_votes,
    }
    return render(request, 'polls/frequency.html', context)


class FrequencyView(generic.DetailView):
    model = Question
    template_name = 'polls/frequency.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = self.object
        choices = question.choice_set.annotate(vote_count=F('votes'))
        context['choices'] = choices
        return context

def add(request):
    return render(request, 'polls/add.html')

def confirm_add(request):
    # récupération du libellé de la question,
    # sans les éventuels espaces avant et après
    question_text = request.POST['question_text'].strip()
    if question_text:
        # ajout de la question si elle n'est pas vide
        question = Question(question_text=question_text,
                     pub_date=timezone.now())
        question.save()
        return render(request, 'polls/confirm_add.html')
    else:
        # réaffichage du formulaire de saisie de la question
        # avec le message d'erreur
        return render(request, 'polls/add.html', {
            'error_message': "You didn't enter a question text",
     })
