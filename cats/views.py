from rest_framework import viewsets

from .models import Cat, Owner, Achievement
from .serializers import CatSerializer, CatListSerializer, OwnerSerializer, AchievmentSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    @action(detail=False, url_path='recent-white-cats')
    def recent_white_cats(self, request):
        cats = Cat.objects.filter(color='White')[:5]
        serializer = self.get_serializer(cats, many=True)
        return Response(serializer.data) 

    def get_serializer_class(self):
        if self.action == 'list':
            return CatListSerializer
        return CatSerializer
    

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer 

class AchievementsSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievmentSerializer


class UpdateDeleteViewSet(mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    pass

class CreateRetrieveViewSet(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    pass

class LightCatViewSet(CreateRetrieveViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    