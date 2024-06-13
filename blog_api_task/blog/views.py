from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def index(request):
    return render(request, 'index.html')

@api_view(['GET'])
def search_posts(request):
    keyword = request.GET.get('keyword')
    if keyword:
        posts = Post.objects.filter(title__icontains=keyword) | Post.objects.filter(content__icontains=keyword)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    else:
        return Response({'message': 'No keyword provided'})