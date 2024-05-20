from django.shortcuts import render 
from .models import Category, Movie

# Create your views here.
# Yaptığınız isteğin ne olduğunu döner, GET,POST v.s.

kategori_liste = ["macera","romantik","dram","bilim kurgu"]
film_liste = [ 
    {
        "id": 1,
        "film_adi": "film1",
        "aciklama": "film1 aciklama",
        "resim": "1.jpg",
        "anasayfa": True,
    },
    {
        "id": 2,
        "film_adi": "film2",
        "aciklama": "film2 aciklama",
        "resim": "2.jpg",
        "anasayfa": True,
    },
    {
        "id": 3,
        "film_adi": "film3",
        "aciklama": "film3 aciklama",
        "resim": "3.jpg",
        "anasayfa" : False,
    },
    {
        "id": 4,
        "film_adi": "film4",
        "aciklama": "film4 aciklama",
        "resim": "1.jpg",
        "anasayfa" : False,
    }
]

def home(request):
    data={
        "kategoriler" : Category.objects.all(),
        "filmler" : Movie.objects.all()
    }
    return render(request, "index.html", data)

def movies(request):
    data={
        "kategoriler" : kategori_liste,
        "filmler" : film_liste
    }
    return render(request, "movies.html", data)

def moviedetails(request, id):
    data={
        "movie": Movie.objects.get(id=id)
    }
    return render(request, "details.html", data)