from rest_framework import serializers
from .models import Comment, Post
from core.models import CustomUser



class GetUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['email',]
        
    def to_representation(self, instance):
        temp = super().to_representation(instance)
        if instance.get_full_name():
            temp['name'] = instance.get_full_name()
        return temp


class PostSerializer(serializers.ModelSerializer):
    author = GetUserSerializer(read_only=True)
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
        return value
        

class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    
    class Meta:
        model = Comment
        fields = '__all__'
        
    def validate_content(self, value):
        if not value:
            raise serializers.ValidationError('Content must be filled!')
        return value