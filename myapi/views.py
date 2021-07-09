from rest_framework import viewsets
from .serializer import PostSerializer
from .models import Post

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer