from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .models import ProductModel
from .serializers import PgSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.



@api_view(['GET','POST'])
@authentication_classes([ JWTAuthentication])
@permission_classes([IsAuthenticated])

def productPage(request):
    if request.user.is_authenticated:

        if request.method == 'GET':

            id=request.user.id

            paginator=PageNumberPagination()
            paginator.page_size=5
            pm = ProductModel.objects.filter(user=id)
            obj=paginator.paginate_queryset(pm,request)

            #print(pm.values())
            pgs=PgSerializer(obj,many=True)

            print(pgs.data)


            return Response(data=pgs.data)

        if request.method=='POST':
            userid=request.user.id
            pd=request.data
            pd['user']=userid
            pgs=PgSerializer(data=pd)
            if pgs.is_valid():
                pgs.save()
                message = {'message': 'Data created successfully...'}

            else:
                message=pgs.errors

            return Response(message)


    else:
        return Response('NO user Logged in...')


