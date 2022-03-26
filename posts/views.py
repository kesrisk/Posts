from turtle import title
from django.shortcuts import render
from rest_framework.views import APIView
from posts.models import Posts
from posts.serializers import PostSerializer
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework import pagination
from django.core.paginator import Paginator
# Create your views here.

class PostsView(APIView, PageNumberPagination):
    queryset = None
    permission_classes = ()
    page_size = 10

    def get(self, request):

        if 'page_size' in request.query_params.keys():
            
            self.page_size = request.query_params['page_size']
 
        queryset = Posts.objects.all()

        page = self.paginate_queryset(queryset, request)

        serializer = PostSerializer(page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request):

        data = request.data

        posts_data = {
            'title': data['title'],
            'description': data['description']
        }
        serializer = PostSerializer(data = posts_data)

        if serializer.is_valid():

            serializer.save()

            return JsonResponse(status=200, data={'success': True, 'data': serializer.data})

        else:
            return JsonResponse(status=422, data={'success': True, 'data': "Invalid data"})


