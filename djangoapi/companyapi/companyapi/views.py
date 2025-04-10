

from django.http import HttpResponse,JsonResponse


def home_page(request):
    print("this is home page")
    avengers = [
        
        'Hawk-eye',
        'Spider-Man',
        'Iron-Man',
        'Hulk',

    ]
    marvelmovie_actor_name={
        "Iron-Man":"Tony stark",
        "Spiderman":"Peter Parker",
        "Captain America":"Steve Rogers",
        "Thor":"Thor-Odinson",
    }
    data ={
        "avenegers":avengers,
        "actors":marvelmovie_actor_name
    }
    return JsonResponse(data,safe=False)