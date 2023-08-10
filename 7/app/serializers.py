from rest_framework import serializers
from .models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    
    class Meta:
        model = Post
        fields = '__all__'
        
    def validate_title(self, value):
        if Post.objects.filter(title=value).exists():
            raise serializers.ValidationError("title must be unique!")
        return value    
    
    def validate_content(self, value):
        if not value:
            raise serializers.ValidationError('Content must be filled!')

class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    
    class Meta:
        model = Comment
        fields = '__all__'
        
    def validate_content(self, value):
        if not value:
            raise serializers.ValidationError('Content must be filled!')