from django.urls import path
import polls.views

urlpatterns = [
    path('', polls.views.index, name='index'),
]