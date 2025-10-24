# polls/models.py

import datetime  # <-- Añadir esta importación
from django.db import models
from django.utils import timezone  # <-- Añadir esta importación

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # --- Añade este método ---
    def __str__(self):
        return self.question_text

    # --- Y añade este método ---
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # --- Añade este método ---
    def __str__(self):
        return self.choice_text