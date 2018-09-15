from django.contrib import admin
from .models import Question, Category, Answer
# Register your models here.
# admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Answer)


class AnswerInline(admin.TabularInline):
    '''Tabular Inline View for Category'''

    model = Answer
    min_num = 1
    max_num = 4



@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """ The Admin view of the Question and related models """


    inlines = [AnswerInline]
    