from django.contrib import admin

from .models import Question
from .models import Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    search_fields = ('question_text',)
    list_filter = ('pub_date',)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'votes', 'question')
    search_fields = ('choice_text',)
    list_filter = ('votes', 'question')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)