from rest_framework import serializers
from .models import Post 

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'text')


#class AuthorSerializer(serializers.ModelSerializer):
    #class Meta:
        #model= Author
        #fields = ('name')