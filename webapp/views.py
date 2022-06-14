from django.shortcuts import render
from days.models import Year, Month, Day, Note


def index(request):
    return render(request, "webapp/index.html", {'years':Year.objects.all()})


def months(request, year):
    return render(request, "webapp/months.html", {'months':Month.objects.filter(
        year= Year.objects.get(id=year)
    )})


def days(request, month):
    return render(request, "webapp/days.html", {'days':Day.objects.filter(
        month= Month.objects.get(id=month)
    )})


def notes(request, day):
    return render(request, "webapp/notes.html", {'notes':Note.objects
    .filter(
        day= Day.objects.get(id=day)
    )
    .filter(
        user= request.user
    )
    })