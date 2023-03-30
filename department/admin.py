from django.contrib import admin
from .models import Department, Worker, Unit, Task, Pastor, Academics


admin.site.register(Department)
admin.site.register(Academics)
admin.site.register(Worker)
admin.site.register(Unit)
admin.site.register(Task)
admin.site.register(Pastor)