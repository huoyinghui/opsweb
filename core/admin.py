# from django.contrib import admin
# from mptt.admin import MPTTModelAdmin
# from import_export import resources
# from .models import PageJson
#
#
# class CustomMPTTModelAdmin(MPTTModelAdmin):
#     # specify pixel amount for this ModelAdmin only:
#     mptt_level_indent = 20
#     list_display = ('id', 'name', 'parent', 'level')
#
#
# class PageJsonResource(resources.ModelResource):
#
#     class Meta:
#         model = PageJson
#         fields = ('id', 'name', 'parent', 'level',)
#
# admin.site.register(PageJson, CustomMPTTModelAdmin)
