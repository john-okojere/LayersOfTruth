from django.contrib import admin
from .models import Department, Worker, Unit, Task, Pastor


admin.site.register(Department)
admin.site.register(Worker)
admin.site.register(Unit)
admin.site.register(Task)
admin.site.register(Pastor)