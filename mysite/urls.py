# mysite/urls.py

from django.contrib import admin
from django.urls import path, include

# --- AÑADE ESTAS LÍNEAS ---
admin.site.site_header = "Administración de Encuestas de InspiredSolutions"
admin.site.site_title = "Portal de Admin (Polls)"
admin.site.index_title = "Bienvenido al Portal de Administración"
# --------------------------

urlpatterns = [
    path("polls/", include("polls.urls")), 
    path("admin/", admin.site.urls),
]