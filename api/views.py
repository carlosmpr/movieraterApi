from rest_framework import viewsets , response , status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from .models import Movie,Rating
from django.contrib.auth.models import User
from .serializers import MovieSerializer, RatingSerializer
# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_clases = (TokenAuthentication)

    @action(detail=True, methods=['post'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:
            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            try: 
                rating = Rating.objects.get(user=user.id, movie =movie.id)
                rating.stars = stars
                serializer = RatingSerializer(rating, many=False)
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message':'Rating updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                Rating.objects.create(user=user.id, movie =movie.id, stars=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {'message':'Rating created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message':'Rate the movie'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_clases = (TokenAuthentication)