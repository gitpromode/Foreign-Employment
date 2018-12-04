from django.urls import path, include
from rest_framework import routers

from . import viewset

router = routers.DefaultRouter()

urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	path('province/', viewset.ProvinceViewSet.as_view({'get': 'list'})),
	path('district/', viewset.DistrictViewSet.as_view({'get': 'list'})),
	path('locgov/', viewset.LocGovViewSet.as_view({'get': 'list'})),
	path('prov-dis/', viewset.ProvDisViewSet.as_view()),
]