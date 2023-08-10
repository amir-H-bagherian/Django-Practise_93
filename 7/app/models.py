from django.db import models
from core.models import CustomUser, BaseModel


class Post(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(to=CustomUser,
                               on_delete=models.SET_NULL,
                               null=True)
    
class Comment(BaseModel):
    post = models.ForeignKey(to=Post,
                             on_delete=models.CASCADE)
    content = models.TextField()