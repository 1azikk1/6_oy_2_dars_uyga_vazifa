from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def calculator(request):
    return render(request, 'calculator.html')


def clock(request):
    return render(request, 'clock.html')


def countdown(request):
    return render(request, 'countdown.html')


def weather(request):
    return render(request, 'weather.html')


def game(request):
    return render(request, 'game.html')


def drawing(request):
    return render(request, 'drawing.html')


def currency(request):
    return render(request, 'currency.html')


def registration(request):
    return render(request, 'registration.html')


def progress_bar(request):
    return render(request, 'bar.html')


def quiz(request):
    return render(request, 'quiz.html')
