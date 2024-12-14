from django.shortcuts import render


def home_page(request):
    """
    Обработчик для домашней страницы.
    """
    return render(request, "lists/home.html")
