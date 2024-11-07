from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


def home_view(request):
    return HttpResponse(
        "<h1>Salom, bu bosh sahifa</h1>"
        "<p>Bugun wiew va url ni o'rganamiz</p>"
    )


def home_2_view(request):
    import datetime
    hozirgi_vaqt = datetime.datetime.now()
    context = {
        "hozirgi_vaqt": hozirgi_vaqt
    }
    return render(request, "home.html", context)


def talabalar_view(request):
    param = request.GET.get('search')
    talabalar = Talaba.objects.all()
    if param:
        talabalar = talabalar.filter(ism__icontains=param)
    context = {
        'talabalar': talabalar
    }
    return render(request, "talabalar.html", context)


def mualliflar(request):
    mualliflar = Muallif.objects.all()
    context = {
        'mualliflar': mualliflar
    }
    return render(request, "mualliflar.html", context)


def deleteStudent(request, id):
    talaba = Talaba.objects.get(id=id)
    talaba.delete()
    return redirect('/talabalar/')


