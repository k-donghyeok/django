from django.contrib import admin
from polls.models import Question,Choice
#from books.models import Book,Author,Publisher
# Register your models here.

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2
class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date','question_text']
    fieldsets = [
        ('Question Statement',{'fields':['question_text']}),
        ('Date Information',{'fields':['pub_date'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']

#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(Publisher)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)

#kdh jambbong1!
