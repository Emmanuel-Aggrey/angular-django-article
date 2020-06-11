from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.permissions import (IsAuthenticatedOrReadOnly)

from .models import Article
from .serializers import ArticleSerializer

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'


class ArticleApiView(generics.ListAPIView, generics.CreateAPIView,
                     generics.RetrieveAPIView, generics.UpdateAPIView,
                     generics.DestroyAPIView):

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'key'
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, key=None):

        if key:
            # return the article

            return self.retrieve(request, key)

        else:
            # all articles
            return self.list(request)

    def post(self, request):
      

        return self.create(request)

    def put(self, request, key=None):
        
        return self.update(request, key=key)

    def delete(self, request, key):
       
        return self.destroy(request, key)

