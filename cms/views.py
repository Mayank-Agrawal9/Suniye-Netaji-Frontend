from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from cms.models import NewsDetail, HomePageP1, City, State, Category
from cms.serializers import CreateNewsDetailSerializer, ListNewsDetailSerializer, HomePageP1Serializer, \
    ListHomePageP1Serializer, CitySerializer, StateSerializer, CategorySerializer, ListCategorySerializer, \
    ListCitySerializer, ListStateSerializer


# Create your views here.


class NewsDetailViewSet(viewsets.ModelViewSet):
    queryset = NewsDetail.objects.publish().select_related('category', 'city', 'author').order_by('-date_created')
    serializer_classes = {
        'create': CreateNewsDetailSerializer,
        'list': ListNewsDetailSerializer,
        'retrieve': ListNewsDetailSerializer
    }
    default_serializer_class = ListNewsDetailSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = {'id': ['exact'], 'category': ['exact'], 'city': ['exact'], 'title': ['icontains'],
                        'author': ['exact']}
    search_fields = ['title', 'content', 'category__name', 'city__name', 'author__first_name',
                     'city__state__name']

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class HomePageP1ViewSet(viewsets.ModelViewSet):
    queryset = HomePageP1.objects.publish().select_related('news_detail').order_by('-date_created')
    serializer_classes = {
        'create': HomePageP1Serializer,
        'list': ListHomePageP1Serializer,
        'retrieve': ListHomePageP1Serializer
    }
    default_serializer_class = ListHomePageP1Serializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = {'id': ['exact'], 'is_p1': ['exact'], 'is_popular': ['exact'], 'is_breaking': ['exact']}
    search_fields = ['news_detail__title', 'content', 'category__name', 'city__name', 'author__first_name',
                     'city__state__name']

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.publish().select_related('state').order_by('-date_created')
    serializer_classes = {
        'create': CitySerializer,
        'list': ListCitySerializer,
        'retrieve': CitySerializer
    }
    default_serializer_class = ListCitySerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = {'state': ['exact']}
    search_fields = ['name', 'title', 'description', 'state__name']

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.publish().order_by('-date_created')
    serializer_classes = {
        'create': StateSerializer,
        'list': ListStateSerializer,
        'retrieve': StateSerializer
    }
    default_serializer_class = StateSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = {'name': ['exact']}
    search_fields = ['name',]

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.publish().order_by('-date_created')
    serializer_classes = {
        'create': CategorySerializer,
        'list': ListCategorySerializer,
        'retrieve': CategorySerializer
    }
    default_serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = {'name': ['icontains']}
    search_fields = ['name', 'title', 'description']

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)