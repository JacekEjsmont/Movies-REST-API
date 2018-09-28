import requests

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters

from .models import Movie, Comment
from .serializers import MovieSerializer, MovieTitleSerializer ,CommentSerializer
# Create your views here.


class MoviesView(APIView):
    queryset = Movie.objects.all()
    serializer_class = MovieTitleSerializer

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        url = 'http://www.omdbapi.com/?t={}&apikey=d2b5785b'
        title = request.data.get('Title')
        movie_details = requests.get(url.format(str(title))).json()

        # validates if movie is found
        if movie_details == {'Response': 'False', 'Error': 'Movie not found!'}:
            return Response({'Error': 'Movie not found'}, status=status.HTTP_400_BAD_REQUEST)

        # validates if movie is already in the base
        if Movie.objects.filter(Title=movie_details['Title']):
            return Response({'Error': 'Movie already in database'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer = MovieSerializer(data=movie_details)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentsView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [filters.SearchFilter,]
    search_fields = ['Movie__id']

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
