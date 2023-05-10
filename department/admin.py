from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportMixin
from django.contrib import admin
from .models import Department, Worker, Unit, Task, Pastor, Academics,ProfilePicture


class DepartmentAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name','hod','description','created_date',)
    list_filter = ('name','hod','description','created_date',)
    search_fields = ('name','hod','description','created_date',)
admin.site.register(Department, DepartmentAdmin)

class AcademicsAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('user','School','matric_number','faculty','department','program','time_table','lvl1_cgpa','lvl2_cgpa','lvl3_cgpa','lvl4_cgpa','lvl5_cgpa')
    list_filter = ('user','School','matric_number','faculty','department','program','time_table','lvl1_cgpa','lvl2_cgpa','lvl3_cgpa','lvl4_cgpa','lvl5_cgpa',)
    search_fields = ('user','School','matric_number','faculty','department','program','time_table','lvl1_cgpa','lvl2_cgpa','lvl3_cgpa','lvl4_cgpa','lvl5_cgpa',)
admin.site.register(Academics, AcademicsAdmin)

class workerAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('user','uid','department','unit','created_date','approved',)
    list_filter = ('user','uid','department','unit','created_date','approved',)
    search_fields = ('user','uid','department','unit','created_date','approved',)
admin.site.register(Worker, workerAdmin)

class UnitAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('department','name','hou','description','created_date',)
    list_filter = ('department','name','hou','description','created_date',)
    search_fields = ('department','name','hou','description','created_date',)
admin.site.register(Unit, UnitAdmin)

class TaskAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('unit','worker','title','description','timefrom','timeto',)
    list_filter = ('unit','worker','title','description','timefrom','timeto',)
    search_fields = ('unit','worker','title','description','timefrom','timeto',)
admin.site.register(Task, TaskAdmin)

class PastorAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('user', 'uid', 'created_date')
    list_filter = ('user', 'uid', 'created_date')
    search_fields = ('user', 'uid', 'created_date')
admin.site.register(Pastor, PastorAdmin)

class Propic(ImportExportMixin, admin.ModelAdmin):
    list_display = ('user','created_date')
    list_filter = ('user','created_date')
    search_fields = ('user','created_date')
admin.site.register(ProfilePicture, Propic)
