from .serializers import SubordinateSerializer
from .models import Subordinate             # data niye ashar jonno
from rest_framework import viewsets, permissions

class SubordinateViewset(viewsets.ModelViewSet):
    queryset=Subordinate.objects.all()       #grab all the entries from subordinate table
    permission_classes=[permissions.AllowAny]
    serializer_class=SubordinateSerializer
