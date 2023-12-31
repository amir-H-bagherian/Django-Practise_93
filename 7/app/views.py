from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status

from .models import Comment, Post
from .serializers import PostSerializer, CommentSerializer

from .permissions import IsOwnerOrReadOnly

class PostView(APIView):
    
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(instance=posts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    
class PostDetailView(APIView):
    
    permission_classes = [IsOwnerOrReadOnly]
    
    def get(self, request, pk):
        post =  get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(instance=post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        post =  get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, post)
        serializer = PostSerializer(instance=post, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        post =  get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, post)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        