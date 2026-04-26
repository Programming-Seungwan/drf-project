from watchlist_app.models import WatchList, StreamingPlatform, Review
from rest_framework.response import Response
from rest_framework import status, generics
from watchlist_app.api.serializers import WatchListSerializer, StreamingPlatformSerializer, ReviewSerializer
from rest_framework.views import APIView

class StreamingListView(APIView):
    def get(self, request):
        streamingPlatformList = StreamingPlatform.objects.all()
        serializer = StreamingPlatformSerializer(streamingPlatformList, many = True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamingPlatformSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



class StreamingDetailView(APIView):
    def get(self, request, pk):
        try:
            streaming = StreamingPlatform.objects.get(pk=pk)
        except StreamingPlatform.DoesNotExist:
            return Response({'Error': 'Streaming Platform Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StreamingPlatformSerializer(streaming)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            streaming = StreamingPlatform.objects.get(pk=pk)
        except StreamingPlatform.DoesNotExist:
            return Response({'Error': 'Streaming Platform Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StreamingPlatformSerializer(streaming, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            streaming = StreamingPlatform.objects.get(pk=pk)
        except StreamingPlatform.DoesNotExist:
            return Response({'Error': 'Streaming Platform Not found'}, status=status.HTTP_404_NOT_FOUND)

        streaming.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListView(APIView):

    def get(self, request):
        watchList = WatchList.objects.all()
        serializer = WatchListSerializer(watchList, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # 내부적으로 Serializer 인스턴스의 create() 메서드를 호출한다.
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailView(APIView):
    def get(self, request, pk):
        try:
            watch = WatchList.objects.get(pk= pk)
        except WatchList.DoesNotExist:
            return Response({'Error' : 'Movie Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerializer(watch)
        return Response(serializer.data)

    def put(self, request, pk):
        watch = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(watch, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        watch = WatchList.objects.get(pk=pk)
        watch.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchList=pk)


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

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