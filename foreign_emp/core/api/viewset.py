from rest_framework import viewsets, serializers
from rest_framework.response import Response
from django.core.serializers import serialize
from core.models import Province, District, LocGov
from .serializers import ProvinceSerializer, DistrictSerializer, LocGovSerializer
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.db.models import Count



class ProvinceViewSet(viewsets.ReadOnlyModelViewSet):
	serializer_class = ProvinceSerializer
	queryset = Province.objects.all()


class DistrictViewSet(viewsets.ReadOnlyModelViewSet):
	serializer_class = DistrictSerializer
	queryset = District.objects.all()


class LocGovViewSet(viewsets.ReadOnlyModelViewSet):
	serializer_class = LocGovSerializer
	queryset = LocGov.objects.all()


class ProvDisViewSet(APIView):

	def get(self, request):
		province_dict = {}
		province_list = []
		dicts = {}

		province = Province.objects.values('name').annotate(number_of_districts=Count('district'))
		# province = District.objects.values('province_id').annotate(Count('province_id')).annotate(total=Count('id')).order_by('province_id')
		for item in province:
			dicts[item['name']] = item['number_of_districts']
		province_list.append(dicts)
		province_dict['province'] = province_list
		return Response(province_dict)
