from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from .models import Movie
from .models import StreamPlateform as Streams
from app.serialize import MovieSerializer,StreamPlateformSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from app.permissions import IsAdminUser
from rest_framework.throttling import UserRateThrottle

# @api_view(['GET', 'POST'])
# def MovieList(request):
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serialize_movies = MovieSerializer(movies, many=True,context={'request': request})
#         return Response(serialize_movies.data)

#     if request.method == "POST":
#         serialize_movie = MovieSerializer(data=request.data,context={'request': request})
#         if serialize_movie.is_valid():
#             serialize_movie.save()
#             return Response(serialize_movie.data, status=201) 
#         else:
#             return Response(serialize_movie.errors, status=400)

class MovieListView(APIView):
    permission_classes = [IsAdminUser]
    throttle_classes = [UserRateThrottle]
    def get(self, request):
        movies = Movie.objects.all()
        movie_serializer = MovieSerializer(movies,many=True, context={'request': request})
        return Response(movie_serializer.data)
    def post(self,request):
        movie_serializer = MovieSerializer(data=request.data)
        if movie_serializer.is_valid():
            movie_serializer.save()
            return Response(movie_serializer.data)
        else:
            return Response(movie_serializer.errors)
    









@api_view(['GET', 'PUT','DELETE'])
def MovieDetail(request,id):
    
    if request.method == "GET":
        try:
            movie =Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            return Response("Movie not Found", status=404)

        serialize_movie = MovieSerializer(movie,context={'request': request})
        return Response(serialize_movie.data)
    if request.method == "PUT":
        try:
            movie =Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            return Response("Movie not Found", status=404)
        serialize_movie = MovieSerializer(movie, data=request.data,context={'request': request})
        if serialize_movie.is_valid():
                serialize_movie.save()
                return Response(serialize_movie.data)
        else:
            return Response(serialize_movie.errors)




    if request.method == "DELETE":
        movie = Movie.objects.get(id=id)
        movie.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def StreamPlateform(request):
    if request.method == "GET":
        plateform = Streams.objects.all()
        serialize_stream = StreamPlateformSerializer(plateform, many=True,context={'request': request})
        return Response(serialize_stream.data)

    if request.method == "POST":
        serialize_stream = StreamPlateformSerializer(data=request.data)
        if serialize_stream.is_valid():
            serialize_stream.save()
            return Response(serialize_stream.data, status=201) 
        else:
            return Response(serialize_stream.errors, status=400)




@api_view(['GET', 'PUT','DELETE'])
def StreamPlateformD(request,id):
    
    if request.method == "GET":
        try:
            plateform =Streams.objects.get(id=id)
        except Streams.DoesNotExist:
            return Response("plateform not Found", status=404)

        serialize_movie = StreamPlateformSerializer(plateform,context={'request': request})
        return Response(serialize_movie.data)
    if request.method == "PUT":
        try:
            plateform =Streams.objects.get(id=id)
        except Streams.DoesNotExist:
            return Response("plateform not Found", status=404)
        serialize_movie = StreamPlateformSerializer(plateform, data=request.data,context={'request': request})
        if serialize_movie.is_valid():
                serialize_movie.save()
                return Response(serialize_movie.data)
        else:
            return Response(serialize_movie.errors)
    
    if request.method == "DELETE":
        plateform = Streams.objects.get(id=id)
        plateform.delete()
        return Response(status=status.HTTP_200_OK)