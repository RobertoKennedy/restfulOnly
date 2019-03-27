from django.shortcuts import render
from rest_framework import viewsets
from .models import Livro
from .serializers import LivroSerializer

class LivroViewSet(viewsets.ModelViewSet):
	querryset = Livro.objects.all()
	serializer_class = LivroSerializer