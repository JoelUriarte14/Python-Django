# polls/urls.py

from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    # 1. Cambiamos views.index por views.IndexView.as_view()
    path("", views.IndexView.as_view(), name="index"),
    
    # 2. Cambiamos question_id por pk y apuntamos a DetailView
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    
    # 3. Cambiamos question_id por pk y apuntamos a ResultsView
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    
    # 4. ¡LA VISTA 'vote' QUEDA IGUAL! Sigue siendo una función.
    path("<int:question_id>/vote/", views.vote, name="vote"),
]