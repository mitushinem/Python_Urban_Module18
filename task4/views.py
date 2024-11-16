from django.shortcuts import render


def index(request):
    context = {
        'title': 'Главная страница',
    }
    return render(request, template_name='fourth_task/index.html', context=context)

def game(request):
    context = {
        'title': 'Игры',
        'games': ['Anatomik Heart', 'Cyberpunk 2077', 'PayDay 2']
    }

    return render(request, template_name='fourth_task/games.html', context=context)

def cart(request):
    context = {
        'title': 'Корзина',
    }
    return render(request, template_name='fourth_task/cart.html', context=context)
