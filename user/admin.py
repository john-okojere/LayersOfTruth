from django.contrib import admin
from .models import  User, Messages, Prayers, OnlineSoul
from import_export.admin import ImportExportMixin



class UserAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('username','first_name','last_name','phone','email','gender','role','is_staff','is_active','date_joined','update_fields',)
    list_filter = ('username','first_name','last_name','phone','email','gender','role','is_staff','is_active','date_joined','update_fields',)
    search_fields = ('username','first_name','last_name','phone','email','gender','role','is_staff','is_active','date_joined','update_fields',)
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)
admin.site.register(User, UserAdmin)


class MAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name','email','message','checked','create_date',)
    list_filter = ('name','email','message','checked','create_date',)
    search_fields = ('name','email','message','checked','create_date',)
admin.site.register(Messages, MAdmin)


class PAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('first_name','last_name','email','phone' ,'request', 'checked', 'create_date',)
    list_filter = ('first_name','last_name','email','phone' ,'request', 'checked', 'create_date',)
    search_fields = ('first_name','last_name','email','phone' ,'request', 'checked', 'create_date',)
admin.site.register(Prayers, PAdmin)


class OAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name','phone','checked','create_date',)
    list_filter = ('name','phone','checked','create_date',)
    search_fields = ('name','phone','checked','create_date',)
admin.site.register(OnlineSoul,OAdmin )