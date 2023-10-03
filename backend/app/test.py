from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import StreamPlateform, Movie,Review
from app.serialize import MovieSerializer, StreamPlateformSerializer,ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import IsAdminUser

class StreamPlatformAV(APIView):

    def get(self, request):
        platform = StreamPlateform.objects.all()
        Serializer = StreamPlateformSerializer(platform, many=True, context={'request': request})
        return Response(Serializer.data)

    def post(self, request):
        serializer = StreamPlateformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamDetailAV(APIView):

    def get(self, request, pk):
        
        try:
            platform = StreamPlateform.objects.get(pk=pk)
        except StreamPlateform.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlateformSerializer(platform,context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        platform = StreamPlateform.objects.get(pk=pk)
        serializer = StreamPlateformSerializer(platform, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        platform = Movie.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class MovieDetailAV(APIView):

    def get(self, request, pk):
        try:
            platform = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(platform)
        return Response(serializer.data)

    def put(self, request, pk):
        platform = StreamPlateform.objects.get(pk=pk)
        serializer = MovieSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        platform = Movie.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewListView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        platform = Review.objects.all()
        Serializer = ReviewSerializer(platform, many=True, context={'request': request})
        return Response(Serializer.data)

    def post(self, request):
        # return Response("you already rated")
        id_m =request.data['movie']

        user_review = self.request.user
        review = Review.objects.filter(movie=id_m, user_review=user_review)
        the_movie = Movie.objects.get(pk=id_m)
        if review.exists():
            return Response("you already rated this movie")
        review_data = request.data.copy()
        review_data['user_review'] = request.user.username
      
        if the_movie.total_rating == 0:
            the_movie.avrg_rating = request.data['rating']
        else:
            the_movie.avrg_rating = (the_movie.avrg_rating + request.data['rating']) / 2
        the_movie.total_rating += 1
        the_movie.save()
        serializer = ReviewSerializer(data=review_data)
        if serializer.is_valid():
            serializer.save(user_review=user_review)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ReviewDetailAV(APIView):

    def get(self, request, pk):
        try:
            platform = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReviewSerializer(platform)
        return Response(serializer.data)

    def put(self, request, pk):
        platform = StreamPlateform.objects.get(pk=pk)
        serializer = ReviewSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        platform = Review.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)