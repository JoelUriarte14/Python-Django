# polls/views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.utils import timezone # Importamos timezone
from django.views import generic # Importamos generic

from .models import Question, Choice

# --- CREAMOS LA VISTA INDEX (BASADA EN CLASES) ---
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Retorna las últimas 5 preguntas publicadas."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by("-pub_date")[:5]

# --- CREAMOS LA VISTA DETAIL (BASADA EN CLASES) ---
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excluye cualquier pregunta que no haya sido publicada aún.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

# --- CREAMOS LA VISTA RESULTS (BASADA EN CLASES) ---
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

# --- LA VISTA 'vote' QUEDA IGUAL (BASADA EN FUNCIONES) ---
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "No seleccionaste una opción.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))