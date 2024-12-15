from import_export import resources
from cms.models import Category, State, HomePageP1, NewsDetail, City

EXCLUDE_FOR_API = ('date_created', 'updated_by', 'date_updated', 'created_by')


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        import_id_fields = ('id',)
        exclude = ('date_created', 'updated_by', 'date_updated', 'created_by', 'image', 'description')


class StateResource(resources.ModelResource):
    class Meta:
        model = State
        import_id_fields = ('id',)
        exclude = EXCLUDE_FOR_API


class CityResource(resources.ModelResource):
    class Meta:
        model = City
        import_id_fields = ('id',)
        exclude = ('description', 'date_created', 'updated_by', 'date_updated', 'created_by')


class NewsDetailResource(resources.ModelResource):
    class Meta:
        model = NewsDetail
        import_id_fields = ('id',)
        fields = ('id', 'category', 'city', 'title', 'tags')


class HomePageP1Resource(resources.ModelResource):
    class Meta:
        model = HomePageP1
        import_id_fields = ('id',)
        exclude = EXCLUDE_FOR_API