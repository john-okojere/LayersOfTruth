from django.contrib import admin
from .models import Attendee, Attendance, Contact, CreateAttendance, WorkerAttendance, PastorAttendance

admin.site.register(Attendee)
admin.site.register(CreateAttendance)
admin.site.register(WorkerAttendance)
admin.site.register(PastorAttendance)
admin.site.register(Attendance)
admin.site.register(Contact)