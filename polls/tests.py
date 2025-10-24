# polls/tests.py

import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse  # <-- AÑADE ESTA IMPORTACIÓN

from .models import Question

# --- ESTA FUNCIÓN HELPER ES NUEVA ---
def create_question(question_text, days):
    """
    Crea una pregunta con el 'question_text' dado y la publica
    el número de 'days' (positivo para el futuro, negativo para el pasado).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionModelTests(TestCase):
    # ... tus 3 tests de antes van aquí ...
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


# --- ESTA NUEVA CLASE DE TESTS VA DEBAJO ---
class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        Si no existen preguntas, se muestra el mensaje apropiado.
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No hay encuestas disponibles.")

    def test_past_question(self):
        """
        Preguntas con pub_date en el pasado se muestran en el index.
        """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_future_question(self):
        """
        Preguntas con pub_date en el futuro NO se muestran en el index.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No hay encuestas disponibles.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

        # polls/tests.py
# ... (todo el código anterior) ...

# --- ESTA NUEVA CLASE DE TESTS VA DEBAJO ---
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        El DetailView de una pregunta con pub_date en el futuro
        debe devolver un 404 (Not Found).
        """
        future_question = create_question(question_text="Future question.", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        El DetailView de una pregunta con pub_date en el pasado
        debe mostrar el texto de la pregunta.
        """
        past_question = create_question(question_text="Past Question.", days=-5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)