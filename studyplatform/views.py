from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import AnkiCard, CardsSet
import random


def anki_card_list(request):
    cards = AnkiCard.objects.all()
    return render(request, 'anki_card_list.html', {'cards': cards})


def create_anki_card(request):
    if request.method == 'POST':
        front_side = request.POST['front_side']
        back_side = request.POST['back_side']
        image = request.POST['image']

        # Дополнительная валидация данных
        if not front_side:
            return render(request, 'error.html', {'message': 'Введите текст для лицевой стороны'})
        if not back_side:
            return render(request, 'error.html', {'message': 'Введите текст для стороны обратной стороны'})

        # Сохранение Anki карточки в базе данных
        card = AnkiCard.objects.create(
            front_side=front_side,
            back_side=back_side,
            image=image
        )
        card.save()
        return redirect('anki_card_created')
    return render(request, 'create_anki_card.html')


def anki_card_created(request):
    return redirect(anki_card_list)


def start_learning(request):
    cards = AnkiCard.objects.all()
    if len(cards) < 20:
        random_cards = cards
    else:
        random_cards = random.sample(list(cards), 20)
    return render(request, 'anki_learning.html', {'cards': random_cards})
