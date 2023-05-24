from rest_framework import viewsets

from .models import Cat, Owner, Achievement
from .serializers import CatSerializer, OwnerSerializer, AchievmentSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer 

class AchievementsSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievmentSerializer