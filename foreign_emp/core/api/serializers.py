from rest_framework import serializers
from django.core.serializers import serialize

from core.models import Province, District, LocGov

class ProvinceSerializer(serializers.ModelSerializer):

	class Meta:
		model = Province
		fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
	province = serializers.CharField(source='province.name')

	class Meta:
		model = District
		fields = '__all__'


class LocGovSerializer(serializers.ModelSerializer):

	class Meta:
		model = LocGov
		fields = '__all__'


class ProvDisSerializer(serializers.ListSerializer):
	province_list = serializers.DictField()