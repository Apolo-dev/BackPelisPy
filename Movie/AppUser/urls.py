from django.urls import path
#from django.urls.resolvers import URLPattern
from .views import UserView

urlpatterns=[
    path('users/', UserView.as_view(), name='user'),
    path('users/<int:id>', UserView.as_view(), name='user_process')

]