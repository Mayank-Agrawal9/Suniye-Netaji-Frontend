from django.contrib.auth.models import User
from rest_framework import serializers
from cms.models import NewsDetail, City, Category, HomePageP1, State


class CreateNewsDetailSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(is_active=True), many=False, required=True)
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.publish(), many=False, required=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.publish(), many=False, required=True)

    class Meta:
        model = NewsDetail
        fields = '__all__'


class ListNewsDetailSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    def get_author(self, obj):
        return {'id': obj.author.id, 'name': obj.author.get_full_name()} if obj.author else None

    def get_city(self, obj):
        return {'id': obj.city.id, 'name': obj.city.name} if obj.city else None

    def get_category(self, obj):
        return {'id': obj.category.id, 'name': obj.category.name} if obj.category else None

    class Meta:
        model = NewsDetail
        exclude = ('date_updated', 'status', 'created_by', 'updated_by', 'meta_title', 'meta_keyword',
                   'meta_description', 'content')


class HomePageP1Serializer(serializers.ModelSerializer):

    class Meta:
        model = HomePageP1
        fields = '__all__'


class ListHomePageP1Serializer(serializers.ModelSerializer):
    news_detail = serializers.SerializerMethodField()

    def get_news_detail(self, obj):
        return {'id': obj.news_detail.id, 'title': obj.news_detail.title, 'image': obj.news_detail.image.url if obj.news_detail.image else None,
                'outer_content': obj.news_detail.outer_page_info}

    class Meta:
        model = HomePageP1
        exclude = ('date_updated', 'status', 'created_by', 'updated_by')


class ListCitySerializer(serializers.ModelSerializer):
    state = serializers.SerializerMethodField()

    def get_state(self, obj):
        return {'name': obj.state.name, 'id': obj.state.id}

    class Meta:
        model = City
        exclude = ('date_updated', 'status', 'description', 'created_by', 'updated_by')


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class ListStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        exclude = ('date_updated', 'status', 'created_by', 'updated_by')


class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = '__all__'


class ListCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ('status', 'description', 'created_by', 'updated_by')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'