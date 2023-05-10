from django.db import models
from user.models import User
from qrcode import *
import uuid
from PIL import Image


class Department(models.Model):
    name = models.CharField(max_length=255)
    hod= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'
    
class Unit(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    hou= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'

class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.UUIDField( default=uuid.uuid4, editable=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True, null=True)
    approved =models.BooleanField(default=False)
    
    def qr_code(self):
        qr_code = make(self.uid)
        basename = str(self.id) + '_QR_CODE.png'
        qr_code.save('media/QR_CODE/Worker/{}'.format(basename))
        return '/media/QR_CODE/Worker/{}'.format(basename)
    
    def save(self,*args, **kwargs):
        self.qr_code()
        super(Worker, self).save(*args, **kwargs)
    def __str__(self) -> str:
        return f'{self.user.last_name} {self.user.first_name} Worker at {self.department} - {self.unit} unit'
    
class ProfilePicture(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profilepic")
    image = models.ImageField(upload_to="profile_pic/%y/%m/%d/")
    created_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{0}".format(self.image)

    def save(self):         
        super(ProfilePicture, self).save()
        image = Image.open(self.image.path)
        (width, height) = image.size     
        size = (100, 100)
        image = image.resize(size)
        image.save(self.image.path)



class Task(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.BooleanField( default = False)
    timefrom = models.CharField(max_length=255)
    timeto = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'
    


class Pastor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="pastor")
    uid = models.UUIDField( default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now=True, null=True)
    
    def qr_code(self):
        qr_code = make(self.uid)
        basename = str(self.user.username) + '_QR_CODE.png'
        qr_code.save('media/QR_CODE/Pastor/{}'.format(basename))
        return '/media/QR_CODE/Pastor/{}'.format(basename)
    
    def save(self,*args, **kwargs):
        self.qr_code()
        super(Pastor, self).save(*args, **kwargs)
    def __str__(self) -> str:
        return f'Pastor {self.user.last_name} {self.user.first_name}'
    
class Academics(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student")
    School = models.CharField(max_length=255)
    matric_number = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    program = models.CharField(max_length=255)
    time_table = models.ImageField(upload_to="timetable")
    lvl1_cgpa = models.CharField(max_length=255, null=True, blank=True)
    lvl2_cgpa = models.CharField(max_length=255, null=True, blank=True)
    lvl3_cgpa = models.CharField(max_length=255, null=True, blank=True)
    lvl4_cgpa = models.CharField(max_length=255, null=True, blank=True)
    lvl5_cgpa = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.username}'
    