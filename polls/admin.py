from django.contrib import admin
import polls.models


class ChoiceInline(admin.TabularInline):
    model = polls.models.Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text', "pub_date"]


admin.site.register(polls.models.Question, QuestionAdmin)


# Register your models here.
