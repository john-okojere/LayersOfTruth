from django.shortcuts import render
from siloam.models import Attendee, Attendance, CreateAttendance, WorkerAttendance,PastorAttendance, SpecialAttendance, Specialcard
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
    if Attendee.objects.filter(uid=pk):
        attendee = Attendee.objects.get(uid=pk)
        if Attendance.objects.filter(attendance=list,attendee=attendee):
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
        else:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    elif Worker.objects.filter(uid=pk) :
        attendee = Worker.objects.get(uid=pk) 
        if WorkerAttendance.objects.filter(attendance=list,worker=attendee):
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
        else:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    elif Pastor.objects.filter(uid=pk):
        attendee = Pastor.objects.get(uid=pk)
        if  PastorAttendance.objects.filter(attendance=list,pastor=attendee):
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
        else:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    elif Specialcard.objects.filter(uid=pk):
        attendee = Specialcard.objects.get(uid=pk)
        if  SpecialAttendance.objects.filter(attendance=list,person=attendee):
            attendances = SpecialAttendance.objects.get(attendance=list,person=attendee)
            if attendances.transport:
                context = {
                    "attendance": f'{attendances.person}\n is to be Accomodated'
                }
            else:
                attendances.transport = True
                attendances.save()
                context = {
                    "attendance": f'{attendances.person} Sign Accomodation Successful'
                }
        else:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    return JsonResponse(context, status=200)
        

def food_verify_card(request, list, pk):
    list = CreateAttendance.objects.get(id=list)
    if Attendee.objects.filter(uid=pk):
        attendee = Attendee.objects.get(uid=pk)
        if  Attendance.objects.filter(attendance=list,attendee=attendee):
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
        else:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    elif  Worker.objects.filter(uid=pk):
        attendee = Worker.objects.get(uid=pk)
        if  WorkerAttendance.objects.filter(attendance=list,worker=attendee):
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
        else:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    elif  Pastor.objects.filter(uid=pk):
        attendee = Pastor.objects.get(uid=pk)
        if PastorAttendance.objects.filter(attendance=list,pastor=attendee):
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
        else:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    elif  Specialcard.objects.filter(uid=pk):
        attendee = Specialcard.objects.get(uid=pk)
        if SpecialAttendance.objects.filter(attendance=list,person=attendee):
            attendances = SpecialAttendance.objects.get(attendance=list,person=attendee)
            if attendances.food:
                context = {
                    "attendance": f'{attendances.person}\n is to be Accomodated'
                }
            else:
                attendances.food = True
                attendances.save()
                context = {
                    "attendance": f'{attendances.person} Sign Accomodation Successful'
                }
        else:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    return JsonResponse(context, status=200)
    

def signout_card(request,list, pk):
    list = CreateAttendance.objects.get(id=list)
    if Attendee.objects.filter(uid=pk):
        attendee = Attendee.objects.get(uid=pk)
        if  Attendance.objects.filter(attendance=list,attendee=attendee):
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
        else:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    elif  Worker.objects.filter(uid=pk):
        attendee = Worker.objects.get(uid=pk)
        if WorkerAttendance.objects.filter(attendance=list,worker=attendee):
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
        else:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    elif Pastor.objects.filter(uid=pk):
        attendee = Pastor.objects.get(uid=pk)
        if PastorAttendance.objects.filter(attendance=list,pastor=attendee):
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
        else:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    elif Specialcard.objects.filter(uid=pk):
        attendee = Specialcard.objects.get(uid=pk)
        if SpecialAttendance.objects.filter(attendance=list,person=attendee):
            attendances = SpecialAttendance.objects.get(attendance=list,person=attendee)
            if attendances.time_out:
                context = {
                    "attendance": f'{attendances.person}\n is to be Accomodated'
                }
            else:
                attendances.time_out = date_time_now
                attendances.save()
                context = {
                    "attendance": f'{attendances.person} Sign Accomodation Successful'
                }
        else:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    
    return JsonResponse(context, status=200)   



def accommodation_card(request,list, pk):
    list = CreateAttendance.objects.get(id=list)
    if Attendee.objects.filter(uid=pk):
        attendee = Attendee.objects.get(uid=pk)
        if Attendance.objects.filter(attendance=list,attendee=attendee):
            attendances = Attendance.objects.get(attendance=list,attendee=attendee)
            if attendances.accomodation:
                context = {
                    "attendance": f'{attendances.attendee}\n is to be Accomodated'
                }
            else:
                attendances.accomodation = True
                attendances.save()
                context = {
                    "attendance": f'{attendances.attendee} Sign Accomodation Successful'
                }
        else:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    elif  Worker.objects.filter(uid=pk):
        attendee = Worker.objects.get(uid=pk)
        if WorkerAttendance.objects.filter(attendance=list,worker=attendee):
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
        else:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    elif  Pastor.objects.filter(uid=pk):
        attendee = Pastor.objects.get(uid=pk)
        if  PastorAttendance.objects.filter(attendance=list,pastor=attendee):
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
        else:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    elif  Specialcard.objects.filter(uid=pk):
        attendee = Specialcard.objects.get(uid=pk)
        if  SpecialAttendance.objects.filter(attendance=list,person=attendee):
            attendances = SpecialAttendance.objects.get(attendance=list,person=attendee)
            if attendances.accomodation:
                context = {
                    "attendance": f'{attendances.person}\n is to be Accomodated'
                }
            else:
                attendances.accomodation = True
                attendances.save()
                context = {
                    "attendance": f'{attendances.person} Sign Accomodation Successful'
                }
        else:
            context = {
                    "attendance": f'{attendee}\n Not registered'
                }
    
    return JsonResponse(context, status=200)   



def verify_card(request,list, uid):
    list = CreateAttendance.objects.get(id=list)
    if Worker.objects.filter(uid=uid):
        person = Worker.objects.get(uid=uid)
        if WorkerAttendance.objects.filter(worker=person, attendance=list):
            attendances = WorkerAttendance.objects.get(worker=person, attendance=list)
        else:
            attendances = WorkerAttendance.objects.create(attendance=list, worker=person, time_in = date_time_now)
        return JsonResponse({"attendance": f'{attendances.worker}'}, status=200)
    elif Attendee.objects.filter(uid=uid):
        person = Attendee.objects.get(uid=uid)
        if Attendance.objects.filter(attendee=person, attendance=list):
            attendances = Attendance.objects.get(attendee=person, attendance=list)
        else:
            attendances = Attendance.objects.create(attendance=list, attendee=person, time_in = date_time_now)
        return JsonResponse({"attendance": f'{attendances.attendee}'}, status=200)
    elif Pastor.objects.filter(uid=uid):
        person = Pastor.objects.get(uid=uid)
        if PastorAttendance.objects.filter(pastor=person, attendance=list):
            attendances = PastorAttendance.objects.get(pastor=person, attendance=list)
        else:
            attendances = PastorAttendance.objects.create(attendance=list, pastor=person, time_in = date_time_now)
        return JsonResponse({"attendance": f'{attendances.pastor}'}, status=200)
    elif Specialcard.objects.filter(uid=uid):
        person = Specialcard.objects.get(uid=uid)
        if SpecialAttendance.objects.filter(person=person, attendance=list):
            attendances = SpecialAttendance.objects.get(person=person, attendance=list)
        else:
            attendances = SpecialAttendance.objects.create(attendance=list, person=person, time_in = date_time_now)
        return JsonResponse({"attendance": f'{attendances.person}'}, status=200)
        



