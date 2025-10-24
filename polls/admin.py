# polls/admin.py

from django.contrib import admin
from .models import Question, Choice  # 1. Importa Choice

# 2. Crea una clase para el admin de Choice
class ChoiceInline(admin.TabularInline): # Puedes usar StackedInline si prefieres
    model = Choice
    extra = 3  # Te da 3 espacios para nuevas opciones por defecto

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "pub_date", "was_published_recently")
    
    # 3. Añade los 'inlines' al admin de Question
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
# 4. Nota: No registramos Choice por separado, porque ya está "inline"