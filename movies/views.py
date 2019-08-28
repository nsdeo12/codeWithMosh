from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404

#import Movie object from model
from .models import Movie

# Create your views here.
def index(request):
    #SELECT * FROM movies_movie WHERE release_year =1998; is equivalent to the following
    #Movie.object.filter(release_year=1998)

    #SELECT * FROM movies_movie WHERE id =1; is equivalent to the following
    #Movie.object.get(id=1)

    # SELECT * FROM movies_movie; is equivalent to the following API
    moviesObject = Movie.objects.all()
    allMovies='  and  '.join([m.title for m in moviesObject])

    #to render it in a template
    #pass the request and the name of the template file
    #create a dictionary and pass a key as movies and values as the moviesObject
    return render(request,'movies/index.html',{'movies':moviesObject})

    return HttpResponse(allMovies)
def detail(request,movie_id):
    # try:
        # movieDetailsObject=Movie.objects.get(id=movie_id)
        movieDetailsObject=get_object_or_404(Movie,id=movie_id)
        return render(request,'movies/details.html',{'movies_details':movieDetailsObject})
        #return HttpResponse(movie_id)

    # except Movie.DoesNotExist:
    #     raise Http404()
    