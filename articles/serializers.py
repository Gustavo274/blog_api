from .models import *
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'

class ArticleCreateSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    keyword = KeywordSerializer(many=True)
    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "subtitle",
            "content",
            "keyword"
        ]
    
    
    def validate_title(self, v):
        if len(v) > 100:
            return serializers.ValidationError(
                "Tamanho máximo do título é 120 caracteres."
            )
        return v
    

class ArticleListSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField(read_only=True)
    keyword = KeywordSerializer(many=True)

    class Meta:
        model = Article
        fields = [
            "id",
            "url",
            "title",
            "subtitle",
            "author",
            "comments",
            "keyword"
        ]

    def get_comments(self, obj):
        qs = Comment.objects.filter(parent=obj).count()
        return qs

    def get_url(self, obj):
        return obj.get_api_url()

class ArticleDetailSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    comments = serializers.SerializerMethodField(read_only=True)
    keyword = KeywordSerializer(many=True)

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "subtitle",
            "content",
            "author",
            "created_at",
            "updated_at",
            "comments",
            "keyword"
        ]

    def get_comments(self, obj):
        qs = Comment.objects.filter(parent=obj)
        try:
            serializer = CommentSerializer(qs, many=True)
        except Exception as e:
            print(e)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "parent",
            "author",
            "content",
            "created_at",
            "updated_at",
        ]


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
