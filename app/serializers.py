from rest_framework import serializers
from app.models import Category, ArticleImages, Article


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('category', 'parent', )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.children.exists():
            representation['children'] = CategorySerializer(instance=instance.children.all(), many=True).data
        return representation


class ArticleImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleImages
        exclude = ('id', )


class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    # category = CategorySerializer(many=False)
    images = ArticleImageSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'description', 'owner', 'category', 'images', )

    def validate(self, attrs):
        print(attrs)
        return attrs

    def create(self, validated_data):
        print(validated_data)
        request = self.context.get('request')
        images_data = request.FILES
        created_post = Article.objects.create(**validated_data)
        print(created_post)
        images_obj = [
            ArticleImages(post=created_post, image=image) for image in images_data.getlist('images')
        ]
        ArticleImages.objects.bulk_create(images_obj)
        return created_post
