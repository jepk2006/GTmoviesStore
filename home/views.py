from django.shortcuts import render
from movies.models import Movie

def index(request):
    random_movies = Movie.objects.order_by('?')[:5]
    
    template_data = {}
    template_data['title'] = 'Movies Store'
    template_data['random_movies'] = random_movies
    return render(request, 'home/index.html', {
        'template_data': template_data
    })

def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, 'home/about.html', {
        'template_data': template_data
    })
