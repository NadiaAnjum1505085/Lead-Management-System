from django.db import router
from rest_framework import urlpatterns,routers
from .api import SubordinateViewset

router=routers.DefaultRouter()
router.register('api/leads',SubordinateViewset,'abc')
urlpatterns=router.urls



