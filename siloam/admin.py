from django.contrib import admin
from .models import Attendee, Attendance, Contact, CreateAttendance, WorkerAttendance, PastorAttendance, Specialcard
from import_export.admin import ImportExportMixin



class sAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('seat_number','uid','full_name','phone','local_assembly','age','gender','state','accomodation','location','created',)
    list_filter = ('seat_number','uid','full_name','phone','local_assembly','age','gender','state','accomodation','location','created')
    search_fields = ('seat_number','uid','full_name','phone','local_assembly','age','gender','state','accomodation','location','created')
admin.site.register(Attendee, sAdmin)

class scAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'title', 'uid', 'preview', 'classname', 'created_date', )
    list_filter = ('name', 'title', 'uid', 'preview', 'classname', 'created_date', )
    search_fields = ('name', 'title', 'uid', 'preview', 'classname', 'created_date', )
admin.site.register(Specialcard, scAdmin)

class WAAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('attendance','worker','accomodation','food','transport','time_in','time_out',)
    list_filter = ('attendance','worker','accomodation','food','transport','time_in','time_out',)
    search_fields = ('attendance','worker','accomodation','food','transport','time_in','time_out',)
admin.site.register(WorkerAttendance, WAAdmin)

class PAAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('attendance','pastor','accomodation','food','transport','time_in','time_out',)
    list_filter = ('attendance','pastor','accomodation','food','transport','time_in','time_out',)
    search_fields = ('attendance','pastor','accomodation','food','transport','time_in','time_out',)
admin.site.register(PastorAttendance, PAAdmin)

class AAAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('attendance','attendee','accomodation','food','transport','time_in','time_out',)
    list_filter = ('attendance','attendee','accomodation','food','transport','time_in','time_out',)
    search_fields = ('attendance','attendee','accomodation','food','transport','time_in','time_out',)
admin.site.register(Attendance, AAAdmin)

class CAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('email', 'created',)
    list_filter = ('email', 'created',)
    search_fields = ('email', 'created',)
admin.site.register(Contact, CAdmin)