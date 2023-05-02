"""studyenglish URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from studyplatform.views import anki_card_list, create_anki_card, anki_card_created, start_learning, set_of_card, create_card_set

urlpatterns = [
    path('ankicards/', anki_card_list, name='anki_card_list'),
    path('create_anki_card/', create_anki_card, name='create_anki_card'),
    path('admin/', admin.site.urls),
    path('anki_card_created/', anki_card_created, name='anki_card_created'),
    path('start_learning/', start_learning, name='start_learning'),
    path('set_of_card/', set_of_card, name='set_of_card'),
    path('create_card_set/', create_card_set, name='create_card_set'),
    #path('card_set_created/', card_set_created, name='card_set_created')
]
