from django.db import models
from django.conf import settings
from qrcode import *
import time
from pathlib import Path
from department.models import Worker, Pastor
import uuid
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

class Attendee(models.Model):
    seat_number = models.IntegerField(null=True, blank=True)
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=255 ,null=True, blank=True)
    phone = models.CharField(max_length=20 ,null=True, blank=True)
    local_assembly = models.CharField(max_length=255 ,null=True, blank=True)
    age = models.CharField(max_length=20 ,null=True, blank=True)
    gender = models.CharField(max_length=20 ,null=True, blank=True)
    state = models.CharField(max_length=20 ,null=True, blank=True)
    accomodation = models.BooleanField(default=False ,null=True, blank=True)
    location = models.CharField(max_length=255 ,null=True, blank=True)
    created = models.DateTimeField(auto_now=True)

    

    def qr_code(self):
        qr_code = make(self.uid)
        basename = str(self.seat_number) + '_QR_CODE.png'
        qr_code.save('media/QR_CODE/participant/{}'.format(basename))
        return '/media/QR_CODE/participant/{}'.format(basename)
    
    def qr_code_id(self):
        return f'Attendee{self.id}'
    
    def save(self,*args, **kwargs):
        self.qr_code()
        super(Attendee, self).save(*args, **kwargs)

    def __str__(self) :
        return f'{self.full_name}, Participant with seat number {self.seat_number}.'

CLASS_NAME = (
    ('headsteward','headsteward'),
    ('guestpastor','guestpastor'),
    ('specialguest','specialguest'),
    ('worker','worker'),
    ('pastor','pastor'),
    ('guest','guest'),
)

class Specialcard(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    preview = models.CharField(max_length=100, null=True, blank=True)
    classname = models.CharField(max_length=20, choices=CLASS_NAME)
    created_date = models.DateTimeField(auto_now=True)

    def qr_code(self):
        qr_code = make(self.uid)
        basename = str(self.id) + '_QR_CODE.png'
        qr_code.save('media/QR_CODE/Special/{}'.format(basename))
        return '/media/QR_CODE/Special/{}'.format(basename)
    
    def qr_code_id(self):
        return f'Specialcard{self.id}'
    
    def save(self,*args, **kwargs):
        self.qr_code()
        super(Specialcard, self).save(*args, **kwargs)

    def __str__(self) :
        return f'{self.name}, Special with seat number {self.id}.'


class CreateAttendance(models.Model):
    title = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title}'


class Attendance(models.Model):
    attendance = models.ForeignKey(CreateAttendance, on_delete=models.CASCADE, default=1, related_name="list")
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    accomodation = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    transport = models.BooleanField(default=False)
    time_in = models.DateTimeField(auto_now=True)
    time_out = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return f'{self.attendee.full_name.title()} seat number {self.attendee.seat_number}.'
    
    def save(self, *args, **kwargs):
        self.created += timedelta(hours=1)
        return super().save(*args, **kwargs)

class WorkerAttendance(models.Model):
    attendance = models.ForeignKey(CreateAttendance, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    accomodation = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    transport = models.BooleanField(default=False)
    time_in = models.DateTimeField(auto_now=True)
    time_out = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return f'{self.worker.user.username.title()} number {self.worker.id}.'

    def save(self, *args, **kwargs):
        self.created += timedelta(hours=1)
        return super().save(*args, **kwargs)

class SpecialAttendance(models.Model):
    attendance = models.ForeignKey(CreateAttendance, on_delete=models.CASCADE)
    person = models.ForeignKey(Specialcard, on_delete=models.CASCADE)
    accomodation = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    transport = models.BooleanField(default=False)
    time_in = models.DateTimeField(auto_now=True)
    time_out = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return f'{self.person.name.title()} number {self.person.id}.'

    def save(self, *args, **kwargs):
        self.created += timedelta(hours=1)
        return super().save(*args, **kwargs)

class PastorAttendance(models.Model):
    attendance = models.ForeignKey(CreateAttendance, on_delete=models.CASCADE)
    pastor = models.ForeignKey(Pastor, on_delete=models.CASCADE)
    accomodation = models.BooleanField(default=False)
    food = models.BooleanField(default=False)
    transport = models.BooleanField(default=False)
    time_in = models.DateTimeField(auto_now=True)
    time_out = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return f'{self.pastor.user.username.title()} number {self.pastor.id}.'

    def save(self, *args, **kwargs):
        self.created += timedelta(hours=1)
        return super().save(*args, **kwargs)

class Contact(models.Model):
    email = models.EmailField()
    created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.email}'
    
