from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.urls import reverse


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'register.html', {'error_message': "Your passwords do not match."})
        elif User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error_message': "Username already exists."})
        elif User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error_message': "Email already exists."})

        user = User.objects.create_user(
            username=username,
            password=password1,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.save()
        return redirect('../polls')

    else:
        return render(request, 'register.html')
