from django.urls import path
import polls.views

app_name = 'polls'
urlpatterns = [
    path('', polls.views.IndexView.as_view(), name='index'),
    path('<int:pk>/', polls.views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', polls.views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', polls.views.vote, name='vote'),
]
