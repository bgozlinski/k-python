# Projekt Django

## Przygotowanie

- tworzymy folder na projekty np. django-projects
- tworzymy w nim folder konkretnego projektu
- w nim tworzymy wirtualne srodowisko


    python -m venv venv

- alternatywnie tworzymy virtualne srodowisko gdzies w strukturze foldetu


    np. ~/virualenvs/
    jesli nasz projekt nazywa djangoi_przyklady
    python -m venv ~/virualenvs/django_przyklady

## aktywacja srodowiska

    mac/linux:
    $ source venv/bin/activate

    windows:
    $ venv\Scripts\activate

tip: moze byc potrzebne 

    Set-ExecutionPolicy Unrestricted -Scope Process


tip: deaktywacja wirtualnego srodowiska to:
    
    (venv) $ deactivate

## instalacja django w wirtualnym srodowisku

    pip install django

## Tworzenie projektu

## po co separowac srodowiska

Powiedzmy ze tworzymy projekty `blog`

Jest 23.07.2022 - aktualnia wersja Django to 4.0.6
W blogu potrzebujemy innych zaleznosci - np. django-cms  aktualna wersja 3.10.1

jest 05.04.2023 - tworze projekt `health`

aktualna werdsja 4.2

lepiej miec dwa niezalezne srodowika z konkretnymi wersjami pod konkretny projekt.

## Tworzenie projektu



