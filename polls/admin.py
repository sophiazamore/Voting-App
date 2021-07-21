from django.contrib import admin
import polls.models

admin.site.register(polls.models.Question)
admin.site.register(polls.models.Choice)
# Register your models here.
