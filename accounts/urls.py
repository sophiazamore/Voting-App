from django.urls import path
import accounts.views

app_name = 'polls'
urlpatterns = [
    path("register", accounts.views.register, name="register")
]
