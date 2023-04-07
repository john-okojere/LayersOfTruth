from django.contrib import admin
from .models import Attendee, Attendance, Contact, CreateAttendance, WorkerAttendance, PastorAttendance, Specialcard


@admin.register(Attendee)
class AttendeAdmin(admin.ModelAdmin):
    list_display = ('id','seat_number', 'full_name', 'phone', 'local_assembly', 'age', 'gender', 'state', 'accomodation', 'location', 'created')
    list_filter = ('full_name', 'age', 'gender', 'accomodation', 'local_assembly')
    search_fields = ('id','full_name', 'age', 'gender', 'accomodation', 'local_assembly')
    ordering = ('id',)

admin.site.register(Specialcard)
admin.site.register(CreateAttendance)
admin.site.register(WorkerAttendance)
admin.site.register(PastorAttendance)
admin.site.register(Attendance)
admin.site.register(Contact)