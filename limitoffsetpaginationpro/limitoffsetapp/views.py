from django.shortcuts import render
from .serializers import EmpSerializer
from .models import Emp
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination

class MyPagination(LimitOffsetPagination):
	default_limit=4
	limit_query_param='limit2',
	offset_query_param='offset2'
	# limit_query_param='mylimit',
	# offset_query_param='myoffset',
	# max_limit=10

class EmpViewset(ModelViewSet):
	queryset = Emp.objects.all()
	serializer_class = EmpSerializer
	pagination_class = MyPagination


# srinivasrao452@gmail.com