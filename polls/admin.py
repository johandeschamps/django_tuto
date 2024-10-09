from django.contrib import admin

from .models import Question
from .models import Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'votes', 'question') 

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)