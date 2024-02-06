from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.response import Response

class ListProjectView(ListAPIView):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer

    


