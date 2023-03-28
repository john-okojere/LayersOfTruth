from django.contrib import admin
from .models import Attendee, Attendance, Contact, CreateAttendance, WorkerAttendance, PastorAttendance


@admin.register(Attendee)
class AttendeAdmin(admin.ModelAdmin):
    list_display = ('seat_number', 'full_name', 'phone', 'local_assembly', 'age', 'gender', 'state', 'accomodation', 'location', 'created')
    list_filter = ('full_name', 'age', 'gender', 'accomodation', 'local_assembly')
    search_fields = ('full_name', 'age', 'gender', 'accomodation', 'local_assembly')
    ordering = ('seat_number',)

admin.site.register(CreateAttendance)
admin.site.register(WorkerAttendance)
admin.site.register(PastorAttendance)
admin.site.register(Attendance)
admin.site.register(Contact)