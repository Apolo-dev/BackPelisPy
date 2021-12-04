from django.http.response import JsonResponse
from django.views import View
from .models import User
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# vistas basadas en clases

class UserView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)





    def get(self, request, id=0):
        if (id > 0):
            usuarios = list(User.objects.filter(id = id).values())
            if len(usuarios)> 0:
                user = usuarios[0]
                datos = {'message': "Success", 'movies': user}
            else:
                datos = {'message': "movie not found..."}
            return JsonResponse(datos)
        users = list(User.objects.values())
        if len(users)>0:
            datos = {'message': "Success", 'movies': users}
        else:
            datos = {'message': "Users not found :("}
        return JsonResponse(datos)






    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        User.objects.create(user_name=jd['user_name'], email=jd['email'], password=jd['password'] )
        datos = {'message':"Success"}
        return JsonResponse(datos)



    def put(self, request, id):
        jd = json.loads(request.body)
        usuarios = list(User.objects.filter(id = id).values())
        if len(usuarios)> 0:
            usuario = User.objects.get(id = id)
            usuario.user_name = jd['user_name']
            usuario.email = jd['email']
            usuario.password = jd['password']
            usuario.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Movies dont found :("}
        return JsonResponse(datos)





    def delete(self, request, id):
        usuarios = list(User.objects.filter(id = id).values())
        if len(usuarios) > 0:
            User.objects.filter(id = id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Movies dont found :("}
        return JsonResponse(datos)