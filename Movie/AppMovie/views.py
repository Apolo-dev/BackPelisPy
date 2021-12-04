#from django.shortcuts import render

from django.http.response import JsonResponse
from django.views import View
from .models import Movie
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# vistas basadas en clases

class MovieView(View):

    # se activa cada ves que hacemos una peticion
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id:int = 0):
        if (id > 0):
            movies = list(Movie.objects.filter(id = id).values())
            if len(movies)> 0:
                movie = movies[0]
                datos = {'message': "Success", 'movies': movie}
            else:
                datos = {'message': "movie not found..."}
            return JsonResponse(datos)
        movies = list(Movie.objects.values())
        if len(movies)>0:
            datos = {'message': "Success", 'movies': movies}
        else:
            datos = {'message': "Movies dont found :("}
        return JsonResponse(datos)



    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        Movie.objects.create(name_movie=jd['name_movie'], genero_movie=jd['genero_movie'], year_movie=jd['year_movie'] )
        datos = {'message':"Success"}
        return JsonResponse(datos)





    def put(self, request, id):
        jd = json.loads(request.body)
        movies = list(Movie.objects.filter(id = id).values())
        if len(movies)> 0:
            movie = Movie.objects.get(id = id)
            movie.name_movie = jd['name_movie']
            movie.genero_movie = jd['genero_movie']
            movie.year_movie = jd['year_movie']
            movie.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Movies dont found :("}
        return JsonResponse(datos)



    def delete(self, request, id):
        movies = list(Movie.objects.filter(id = id).values())
        if len(movies) > 0:
            Movie.objects.filter(id = id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Movies dont found :("}
        return JsonResponse(datos)
