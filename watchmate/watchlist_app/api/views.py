from watchlist_app.models import Movie
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.views import APIView

class MovieListView(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # 내부적으로 Serializer 인스턴스의 create() 메서드를 호출한다.
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class MovieDetailView(APIView):
    def get(self, request, pk):
        try:
            movies = Movie.objects.get(pk= pk)
        except Movie.DoesNotExist:
            return Response({'Error' : 'Movie Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movies)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)

#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save() # 내부적으로 Serializer 인스턴스의 create() 메서드를 호출한다.
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, pk):
#     if request.method == 'GET':
#         try:
#             movies = Movie.objects.get(pk= pk)
#         except Movie.DoesNotExist:
#             return Response({'Error' : 'Movie Not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = MovieSerializer(movies)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)