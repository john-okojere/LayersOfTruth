from django.shortcuts import render, redirect, get_object_or_404
from .models import Attendee, Attendance, Contact, CreateAttendance, WorkerAttendance, PastorAttendance, Specialcard, SpecialAttendance
from department.models import Worker, Pastor
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.core.serializers import serialize
from django.db.models import Q
from .forms import CardForm

def registerSiloam(request):
    if request.method =="POST":
        try:
            last_person = Attendee.objects.last().id
        except:
            last_person = 0 
        seat = last_person + 1
        if  request.POST.get('accomodation') == 'on':
            accomodation = True
        else:
            accomodation = False
        attendee = Attendee.objects.create(
            seat_number = '%03d' % seat,
            full_name = request.POST.get('full_name'),
            phone = request.POST.get('phone'),
            local_assembly = request.POST.get('local_assembly'),
            age = request.POST.get('age_range'),
            gender = request.POST.get('gender'),
            state = request.POST.get('state'),
            accomodation = accomodation,
            location = request.POST.get('location'),)
        attendee.save()
        
        return redirect('siloam-tag', pk = attendee.seat_number)
        
    return render(request, 'siloam/index.html')

def registeredlist(request):
    registered = Attendee.objects.all()
    
    return render(request, 'siloam/dashboard/registered.html',{'registered':registered})

def SiloamTag(request, pk):
    attendee = Attendee.objects.get(seat_number=pk)
    if len(str(abs(attendee.seat_number))) == 3:
        zeros = ""
    elif len(str(abs(attendee.seat_number))) == 2:
        zeros = "0"
    elif len(str(abs(attendee.seat_number))) == 1:
        zeros = "00"
    seat_no = zeros+str(attendee.seat_number) 
    return render(request, 'siloam/tag/index.html', {'attendee':attendee, 'seat_no':seat_no})

@login_required
def siloamtags(request):
    attendance = Attendee.objects.all()
    for att in attendance:
        if len(str(abs(att.id))) == 4:
            zeros = ""
        elif len(str(abs(att.id))) == 3:
            zeros = "0"
        elif len(str(abs(att.id))) == 2:
            zeros = "00"
        elif len(str(abs(att.id))) == 1:
            zeros = "000"
        att.id = zeros + str(att.id)
    return render(request, 'siloam/tag/tags.html', {'attendance':attendance})

@login_required
def workerstags(request):
    attendance = Worker.objects.all()
    for att in attendance:
        if len(str(abs(att.id))) == 4:
            zeros = ""
        elif len(str(abs(att.id))) == 3:
            zeros = "0"
        elif len(str(abs(att.id))) == 2:
            zeros = "00"
        elif len(str(abs(att.id))) == 1:
            zeros = "000"
        att.id = zeros+str(att.id) 
    return render(request, 'siloam/tag/workers_tag.html', {'attendance':attendance})


@login_required
def specialstags(request):
    attendance = Specialcard.objects.all()
    for att in attendance:
        if len(str(abs(att.id))) == 4:
            zeros = ""
        elif len(str(abs(att.id))) == 3:
            zeros = "0"
        elif len(str(abs(att.id))) == 2:
            zeros = "00"
        elif len(str(abs(att.id))) == 1:
            zeros = "000"
        att.id = zeros + str(att.id)
    return render(request, 'siloam/tag/special.html', {'attendance':attendance})

def addspecialcard(request):
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('special-tags')
    else:
        form = CardForm()
    return render(request, 'siloam/tag/special_tag_form.html', {'form':form})


@login_required
def pastorstags(request):
    attendance = Pastor.objects.all()
    for att in attendance:
        if len(str(abs(att.id))) == 4:
            zeros = ""
        elif len(str(abs(att.id))) == 3:
            zeros = "0"
        elif len(str(abs(att.id))) == 2:
            zeros = "00"
        elif len(str(abs(att.id))) == 1:
            zeros = "000"
        att.id = zeros + str(att.id)
    return render(request, 'siloam/tag/pastors_tag.html', {'attendance':attendance})


@login_required
def AttendancDetailList(request, pk):
    lists = CreateAttendance.objects.get(id=pk)
    attendance = Attendance.objects.filter(attendance=lists)
    
    return render(request, 'siloam/dashboard/attendace.html', {'list':lists,'attendance':attendance})



@login_required
def PastorAttendanceList(request):
    attendance = CreateAttendance.objects.all().order_by('-created_date')
    return render(request, 'siloam/dashboard/Pastor_attendace_list.html', {'attendance':attendance})


@login_required
def PastorAttendanceDetailList(request, pk):
    lists = CreateAttendance.objects.get(id=pk)
    attendance = PastorAttendance.objects.filter(attendance=lists)
   
    return render(request, 'siloam/dashboard/Pastor_attendace.html', {'list':lists,'attendance':attendance})


@login_required
def SpecialAttendanceList(request):
    attendance = CreateAttendance.objects.all().order_by('-created_date')
    return render(request, 'siloam/dashboard/Special_attendace_list.html', {'attendance':attendance})


@login_required
def SpecialAttendanceDetailList(request, pk):
    lists = CreateAttendance.objects.get(id=pk)
    attendance = SpecialAttendance.objects.filter(attendance=lists)
   
    return render(request, 'siloam/dashboard/Special_attendace.html', {'list':lists,'attendance':attendance})


@login_required
def WorkerAttendanceList(request):
    attendance = CreateAttendance.objects.all().order_by('-created_date')
    return render(request, 'siloam/dashboard/worker_attendace_list.html', {'attendance':attendance})


@login_required
def WorkerAttendanceDetailList(request, pk):
    lists = CreateAttendance.objects.get(id=pk)
    attendance = WorkerAttendance.objects.filter(attendance=lists)
   
    return render(request, 'siloam/dashboard/worker_attendace.html', {'list':lists,'attendance':attendance})


@login_required
def AttendanceList(request):
    attendance = CreateAttendance.objects.all().order_by('-created_date')
    return render(request, 'siloam/dashboard/attendace_list.html', {'attendance':attendance})


@login_required
def siloamDashboard(request):
    attendee = Attendee.objects.all()
    attendance = Attendance.objects.all()
    attendancelist = CreateAttendance.objects.all()
    contact = Contact.objects.all()
    return render(request, 'siloam/dashboard/index.html', {'attendance':attendance,'attendancelist':attendancelist, 'attendee':attendee, 'contact':contact})

def emailContact(request):
    email = request.POST.get('contact_email')
    Contact.objects.create(email=email)
    messages.success(request, 'You have successfully subscribed to siloam update')
    return redirect('siloam')

def email_list(request):
    email = Contact.objects.all()
    return render(request, 'siloam/dashboard/email_list.html', {'email':email})

def createAttendance(request):
    title = request.POST.get('attendancetitle')
    attendance = CreateAttendance.objects.create(title=title)
    return redirect('siloam-attendance-list')

def search_attendancelist(request, name):
    if name.__len__() > 0:
        attendances = CreateAttendance.objects.filter(Q(title__icontains=name))
    else:
        attendances = CreateAttendance.objects.all()
    data = []
    for attendance in attendances:
        data.append({
            "id":attendance.id,
            "title":attendance.title,
            "date":attendance.created_date,
        })
    return JsonResponse(data,safe=False, status=200)
    

def search_registeredlist(request, name):
    if name.__len__() > 0:
        attendances = Attendee.objects.filter(Q(full_name__icontains=name))
    else:
        attendances = Attendee.objects.all()
    data = []
    for attendance in attendances:
        data.append({
            "id":attendance.id,
            'name':attendance.full_name,
            "phone":attendance.phone,
            'accomodation':attendance.accomodation,
            'location':attendance.location,
            "date":attendance.created,
        })
    return JsonResponse(data,safe=False, status=200)
    


def search_attendance(request, name):
    if name.__len__() > 0:
        attendances = Attendance.objects.filter(Q(attendee__full_name__icontains=name))
    else:
        attendances =Attendance.objects.all()
    data = []
    for attendance in attendances:
        if attendance.time_in:
            tin = attendance.time_in.time()
        else:
            tin = "null"

        if attendance.time_out:
            tout = attendance.time_out.time()
        else:
            tout = "null"

        if attendance.food:
            f = "Yes"
        else:
            f = "No"
        if attendance.transport:
            t = "Yes"
        else:
            t = "No"
        if attendance.accomodation:
            a = "Yes"
        else:
            a = "No"
        data.append({
            "id":attendance.id,
            "full_name":attendance.attendee.full_name,
            "time_in":tin,
            "time_out":tout,
            "transport":t,
            "food":f,
            "accomodation":a
        })
    return JsonResponse(data,safe=False, status=200)
    


def Worker_search_attendance(request, name):
    if name.__len__() > 0:
        attendances = WorkerAttendance.objects.filter(Q(worker__user__username__icontains=name))
    else:
        attendances =WorkerAttendance.objects.all()
    data = []
    for attendance in attendances:
        if attendance.time_in:
            tin = attendance.time_in.time()
        else:
            tin = "null"

        if attendance.time_out:
            tout = attendance.time_out.time()
        else:
            tout = "null"

        if attendance.food:
            f = "Yes"
        else:
            f = "No"
        if attendance.transport:
            t = "Yes"
        else:
            t = "No"
        if attendance.accomodation:
            a = "Yes"
        else:
            a = "No"
        data.append({
            "id":attendance.id,
            "username":attendance.worker.user.username,
            "last_name":attendance.worker.user.last_name,
            "first_name":attendance.worker.user.first_name,
            "department":attendance.worker.department.name,
            "unit":attendance.worker.unit.name,
            "time_in":tin,
            "time_out":tout,
            "transport":t,
            "food":f,
            "accomodation":a
        })
    return JsonResponse(data,safe=False, status=200)

