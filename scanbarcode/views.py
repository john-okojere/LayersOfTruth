from django.shortcuts import render
from siloam.models import Attendee, Attendance, CreateAttendance, WorkerAttendance,PastorAttendance
from django.http import JsonResponse
from django.core import serializers
from department.models import Worker, Pastor
from datetime import datetime, timezone

date_time_now = datetime.now(tz=timezone.utc)

def Attendance_scanner(request, pk):
    attendance = CreateAttendance.objects.get(id=pk)
    return render(request, 'scanbarcode/index.html',{'attendance':attendance})
def Transport_scanner(request, pk):
    attendance = CreateAttendance.objects.get(id=pk)
    return render(request, 'scanbarcode/transport.html',{'attendance':attendance})
def Food_scanner(request, pk):
    attendance = CreateAttendance.objects.get(id=pk)
    return render(request, 'scanbarcode/food.html',{'attendance':attendance})
def Signout_scanner(request, pk):
    attendance = CreateAttendance.objects.get(id=pk)
    return render(request, 'scanbarcode/signout.html',{'attendance':attendance})
def Accommodation_scanner(request, pk):
    attendance = CreateAttendance.objects.get(id=pk)
    return render(request, 'scanbarcode/accomodation.html',{'attendance':attendance})


def transport_verify_card(request,list, pk):
    list = CreateAttendance.objects.get(id=list)
    try:
        attendee = Attendee.objects.get(uid=pk)
        try:
            attendances = Attendance.objects.get(attendance=list,attendee=attendee)
            if attendances.transport == True:
                context = {
                    "attendance": f'{attendances.attendee}\n Has used transport'
                }
            else:
                attendances.transport = True
                attendances.save()
                context = {
                    "attendance": f'{attendances.attendee}'
                }
        except:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    except:
        attendee = Worker.objects.get(uid=pk) 
        try:
            attendances = WorkerAttendance.objects.get(attendance=list,worker=attendee)
            if attendances.transport == True:
                context = {
                    "attendance": f'{attendances.worker}\n Has used transport'
                }
            else:
                attendances.transport = True
                attendances.save()
                context = {
                    "attendance": f'{attendances.worker}'
                }
        except:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    finally:
        attendee = Pastor.objects.get(uid=pk)
        try:
            attendances = PastorAttendance.objects.get(attendance=list,pastor=attendee)
            if attendances.transport:
                context = {
                    "attendance": f'{attendances.pastor}\n is to be Accomodated'
                }
            else:
                attendances.transport = True
                attendances.save()
                context = {
                    "attendance": f'{attendances.pastor} Sign Accomodation Successful'
                }
        except:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    
    return JsonResponse(context, status=200)
        

def food_verify_card(request, list, pk):
    list = CreateAttendance.objects.get(id=list)
    try:
        attendee = Attendee.objects.get(uid=pk)
        try:
            attendances = Attendance.objects.get(attendance=list,attendee=attendee)
            if attendances.food == True:
                context = {
                    "attendance": f'{attendances.attendee}\n Has eaten'
                }
            else:
                attendances.food = True
                attendances.save()
                context = {
                    "attendance": f'{attendances.attendee}'
                }
        except:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    except:
        attendee = Worker.objects.get(uid=pk)
        try:
            attendances = WorkerAttendance.objects.get(attendance=list,worker=attendee)
            if attendances.food == True:
                context = {
                    "attendance": f'{attendances.worker}\n Has eaten'
                }
            else:
                attendances.food = True
                attendances.save()
                context = {
                    "attendance": f'{attendances.worker}'
                }
        except:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    finally:
        attendee = Pastor.objects.get(uid=pk)
        try:
            attendances = PastorAttendance.objects.get(attendance=list,pastor=attendee)
            if attendances.food:
                context = {
                    "attendance": f'{attendances.pastor}\n is to be Accomodated'
                }
            else:
                attendances.food = True
                attendances.save()
                context = {
                    "attendance": f'{attendances.pastor} Sign Accomodation Successful'
                }
        except:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    
    return JsonResponse(context, status=200)
    

def signout_card(request,list, pk):
    list = CreateAttendance.objects.get(id=list)
    try:
        attendee = Attendee.objects.get(uid=pk)
        try:
            attendances = Attendance.objects.get(attendance=list,attendee=attendee)
            if attendances.time_out:
                context = {
                    "attendance": f'{attendances.attendee}\n Has signed out already'
                }
            else:
                attendances.time_out = date_time_now
                attendances.save()
                context = {
                    "attendance": f'{attendances.attendee} Sign Out Successful'
                }
        except:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    except:
        attendee = Worker.objects.get(uid=pk)
        try:
            attendances = WorkerAttendance.objects.get(attendance=list,worker=attendee)
            if attendances.time_out:
                context = {
                    "attendance": f'{attendances.worker}\n Has signed out already'
                }
            else:
                attendances.time_out = date_time_now
                attendances.save()
                context = {
                    "attendance": f'{attendances.worker} Sign Out Successful'
                }
        except:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    finally:
        attendee = Pastor.objects.get(uid=pk)
        try:
            attendances = PastorAttendance.objects.get(attendance=list,pastor=attendee)
            if attendances.time_out:
                context = {
                    "attendance": f'{attendances.pastor}\n is to be Accomodated'
                }
            else:
                attendances.time_out = date_time_now
                attendances.save()
                context = {
                    "attendance": f'{attendances.pastor} Sign Accomodation Successful'
                }
        except:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    
    return JsonResponse(context, status=200)   



def accommodation_card(request,list, pk):
    list = CreateAttendance.objects.get(id=list)
    try:
        attendee = Attendee.objects.get(uid=pk)
        try:
            attendances = Attendance.objects.get(attendance=list,attendee=attendee)
            if attendances.time_out:
                context = {
                    "attendance": f'{attendances.attendee}\n is to be Accomodated'
                }
            else:
                attendances.accomodation = True
                attendances.save()
                context = {
                    "attendance": f'{attendances.attendee} Sign Accomodation Successful'
                }
        except:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    except:
        attendee = Worker.objects.get(uid=pk)
        try:
            attendances = WorkerAttendance.objects.get(attendance=list,worker=attendee)
            if attendances.accomodation:
                context = {
                    "attendance": f'{attendances.worker}\n is to be Accomodated'
                }
            else:
                attendances.accomodation = True
                attendances.save()
                context = {
                    "attendance": f'{attendances.worker} Sign Accomodation Successful'
                }
        except:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    finally:
        attendee = Pastor.objects.get(uid=pk)
        try:
            attendances = PastorAttendance.objects.get(attendance=list,pastor=attendee)
            if attendances.accomodation:
                context = {
                    "attendance": f'{attendances.pastor}\n is to be Accomodated'
                }
            else:
                attendances.accomodation = True
                attendances.save()
                context = {
                    "attendance": f'{attendances.pastor} Sign Accomodation Successful'
                }
        except:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    
    return JsonResponse(context, status=200)   



def verify_card(request,list, uid):
    list = CreateAttendance.objects.get(id=list)
    if Worker.objects.get(uid=uid):
        person = Worker.objects.get(uid=uid)
        try:
            attendances = WorkerAttendance.objects.get(worker=person, attendance=list)
        except:
            attendances = WorkerAttendance.objects.create(attendance=list, worker=person, time_in = date_time_now)
        return JsonResponse({"attendance": f'{attendances.worker}'}, status=200)
    elif Attendee.objects.get(uid=uid):
        person = Attendee.objects.get(uid=uid)
        try:
            attendances = Attendance.objects.get(attendee=person, attendance=list)
        except:
            attendances = Attendance.objects.create(attendance=list, attendee=person, time_in = date_time_now)
        return JsonResponse({"attendance": f'{attendances.attendee}'}, status=200)
    elif Pastor.objects.get(uid=uid):
        person = Pastor.objects.get(uid=uid)
        try:
            attendances = PastorAttendance.objects.get(pastor=person, Pastorattendance=list)
        except:
            attendances = PastorAttendance.objects.create(attendance=list, pastor=person, time_in = date_time_now)
        return JsonResponse({"attendance": f'{attendances.attendee}'}, status=200)
        

