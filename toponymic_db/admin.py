from django.contrib import admin

from .models import Language, SourceReferences, MotivationTypes, GeoTypes, Maps


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('language_iso', 'language_name_ru', 'language_name_en')
    list_filter = ['language_iso', 'language_name_ru', 'language_name_en' ]
    search_fields = ['language_iso', 'language_name_ru', 'language_name_en']

class SourceReferencesAdmin(admin.ModelAdmin):
    list_display = ('source_full_description',)
    search_fields = ['source_full_description']

class MotivationTypesAdmin(admin.ModelAdmin):
    list_display = ('motivation_short_name_ru', 'motivation_short_name_en',
                    'motivation_comment_ru', 'motivation_comment_en')
    search_fields = ['motivation_short_name_ru', 'motivation_short_name_en',
                    'motivation_comment_ru', 'motivation_comment_en']

class GeoTypesAdmin(admin.ModelAdmin):
    list_display = ('geotype_ru', 'geotype_en',
                    'geotype_description_ru', 'geotype_description_en')
    search_fields = ['geotype_ru', 'geotype_en',
                    'geotype_description_ru', 'geotype_description_en']

class MapsAdmin(admin.ModelAdmin):
    list_display = ('area_name_ru', 'area_name_en',)
    search_fields = ['area_name_ru', 'area_name_en']

admin.site.register(Language, LanguageAdmin)
admin.site.register(SourceReferences, SourceReferencesAdmin)
admin.site.register(MotivationTypes, MotivationTypesAdmin)
admin.site.register(GeoTypes, GeoTypesAdmin)
admin.site.register(Maps, MapsAdmin)