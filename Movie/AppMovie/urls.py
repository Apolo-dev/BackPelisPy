from django.urls import path
from django.urls.resolvers import URLPattern
from .views import MovieView

urlpatterns=[
    path('movies/', MovieView.as_view(), name='movie'),
    path('movies/<int:id>', MovieView.as_view(), name='movie_process'),
]