from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from cms.models import HomePageP1, NewsDetail, City, State, Category
from cms.resources import EXCLUDE_FOR_API, CategoryResource, StateResource, CityResource, HomePageP1Resource, \
    NewsDetailResource


# Register your models here.

class CustomModelAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name not in EXCLUDE_FOR_API]
        super(CustomModelAdminMixin, self).__init__(model, admin_site)


@admin.register(Category)
class CategoryAdmin(CustomModelAdminMixin, ImportExportModelAdmin):
    resource_class = CategoryResource
    search_fields = ['name', 'title']
    raw_id_fields = ('created_by', 'updated_by')
    list_filter = ('status', )


@admin.register(State)
class StateAdmin(CustomModelAdminMixin, ImportExportModelAdmin):
    resource_class = StateResource
    search_fields = ['name',]
    raw_id_fields = ('created_by', 'updated_by')
    list_filter = ('status', )


@admin.register(City)
class CityAdmin(CustomModelAdminMixin, ImportExportModelAdmin):
    resource_class = CityResource
    search_fields = ['name', 'title']
    raw_id_fields = ('created_by', 'updated_by', 'state')
    list_filter = ('status', )


@admin.register(NewsDetail)
class NewsDetailAdmin(CustomModelAdminMixin, ImportExportModelAdmin):
    resource_class = NewsDetailResource
    search_fields = ['title', ]
    raw_id_fields = ('created_by', 'updated_by', 'category', 'city', 'author')
    list_filter = ('status', )


@admin.register(HomePageP1)
class HomePageP1Admin(CustomModelAdminMixin, ImportExportModelAdmin):
    resource_class = HomePageP1Resource
    raw_id_fields = ('created_by', 'updated_by', 'news_detail')
    list_filter = ('status', )