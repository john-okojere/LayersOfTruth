from django.shortcuts import render, redirect
from .models import Department, Unit, Worker, Task, Pastor
from user.models import User
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from .forms import AcademicForm

def departmentDashboard(request):
    dept = Department.objects.all()
    return render(request, 'department/dashboard/index.html', {'dept':dept})

def createDepartment(request):
    if request.method =="POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        dept = Department.objects.create(name=name,description=description)
        dept.save()
        return JsonResponse({'post':'success', 'id':dept.id})
    return JsonResponse({'post':'false'})

def departmentview(request, pk):
    dept = Department.objects.get(pk=pk)
    return render(request, 'department/index.html', {'dept':dept})


def unitDashboard(request, pk):
    dept = Department.objects.get(pk=pk)
    unit = Unit.objects.filter(department=dept)
    return render(request, 'unit/dashboard/index.html', {'dept':dept,'unit':unit})

def createunit(request, pk):
    dept = Department.objects.get(pk=pk)
    if request.method =="POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        dept = Unit.objects.create(department=dept,name=name,description=description)
        dept.save()
        return JsonResponse({'post':'success', 'id':dept.id})
    return JsonResponse({'post':'false'})

def unitview(request, pk, unit):
    dept = Department.objects.get(pk=pk)
    unit = Unit.objects.get(pk=unit)
    worker = Worker.objects.filter(unit=unit)
    return render(request, 'unit/index.html', {'dept':dept,'unit':unit,'worker':worker})


def workersform(request):
    dept = Department.objects.all()
    return render(request, 'department/form.html',{'dept':dept})

def joinDept(request):
    dept = request.POST.get('dept')
    deptv = Department.objects.get(pk=dept)
    unit = request.POST.get('unit')
    unitv = Unit.objects.get(pk=unit)
    worker = Worker.objects.create(user=request.user,department=deptv,unit=unitv )
    worker.save()
    return redirect('profile')

def getunits(request, pk):
    dept = Department.objects.get(pk=pk)
    unit = Unit.objects.filter(department=dept)
    units =[]
    for unit in unit:
        context = {
            'id' : unit.id,
            'name':unit.name
        } 
        units.append(context)
    return JsonResponse({'unit':units})

def workerslist(request):
    worker = Worker.objects.filter(approved=True)
    return render(request, 'department/workers.html',{'worker':worker})

def deptworkerlist(request, pk):
    dept = Department.objects.get(pk=pk)
    worker = Worker.objects.filter(approved=False, department=dept)
    return render(request, 'department/dept_workers.html',{'worker':worker,'dept':dept})

def pendingworkerslist(request):
    worker = Worker.objects.filter(approved=False)
    return render(request, 'department/workers _pending.html',{'worker':worker})

def approvedworkerslist(request, pk):
    dept = Department.objects.get(pk=pk)
    worker = Worker.objects.filter(approved=True, department=dept)
    return render(request, 'department/deptworkers.html',{'worker':worker, 'dept':dept})

def approveworker(request, pk):
    worker = Worker.objects.get(pk=pk)
    worker.approved = True
    user = User.objects.get(id = worker.user.pk)
    user.role = "WORKER"
    user.save()
    worker.save()
    return JsonResponse({'sucess':"success"})

def search_worker(request,name):
    if name.__len__() > 0:
        worker = Worker.objects.filter(Q(user__username__icontains=name))
    else:
        worker = Worker.objects.all()
    workers = []
    for worker in worker:
        context= {
            "id":worker.id,
            "username":worker.user.username,
            "first_name":worker.user.first_name,
            "last_name":worker.user.last_name,
            "phone":worker.user.phone,
             "email":worker.user.email ,
             "department":worker.department.name ,
             "unit":worker.unit.name ,
             "created_date":worker.created_date ,
        }
        if worker.approved == False:
            workers.append(context)
    return JsonResponse(workers, safe=False)


def asearch_worker(request,name):
    if name.__len__() >0:
        worker = Worker.objects.filter(Q(user__username__icontains=name))
    else:
        worker = Worker.objects.all()
    workers = []
    for worker in worker:
        context= {
            "id":worker.id,
            "username":worker.user.username,
            "first_name":worker.user.first_name,
            "last_name":worker.user.last_name,
            "phone":worker.user.phone,
             "email":worker.user.email ,
             "department":worker.department.name ,
             "unit":worker.unit.name ,
             "created_date":worker.created_date ,
        }
        if worker.approved == True:
            workers.append(context)
    return JsonResponse(workers, safe=False)


def createTask(request, unit):
    units = Unit.objects.get(pk=unit)
    worker = request.POST.get('worker')
    workers = Worker.objects.get(pk=worker)
    title = request.POST.get('title')
    description = request.POST.get('description')
    timefrom = request.POST.get('timefrom')
    timeto = request.POST.get('timeto')

    task = Task.objects.create(unit=units, worker=workers, title=title, description=description, timefrom=timefrom, timeto=timeto)
    task.save()
    return JsonResponse({"message":"success", 'id':task.id})

def ListTask(request, unit):
    units = Unit.objects.get(pk=unit)
    task = Task.objects.filter(unit=units)
    return render(request, 'unit/task_list.html', {'task':task, 'unit':units})



def unitmember(request, unit):
    units = Unit.objects.get(pk=unit)
    worker = Worker.objects.filter(unit=units)
    return render(request, 'unit/unitmember.html', {'worker':worker, 'unit':units})



def listofHod(request):
    depts = Department.objects.all()
    workers = Worker.objects.filter(approved=True)
    return render(request, 'department/hods.html', {'dept':depts, 'workers':workers})

def addHod(request, pk, worker):
    dept = Department.objects.get(pk=pk)
    worker = Worker.objects.get(pk=worker)
    dept.hod = worker.user
    user = User.objects.get(id = dept.hod.pk)
    user.role ="HOD"
    user.save()
    dept.save()
    context = {
        'dept':dept.name,
        'username':dept.hod.username,
        'first_name':dept.hod.first_name,
        'last_name':dept.hod.last_name,
        'phone':dept.hod.phone,
    }
    return JsonResponse(context, safe=False)


def listofPastors(request):
    pastors = Pastor.objects.all()
    return render(request, 'department/pastors.html', {'pastors':pastors})

def addPastor(request, pk):
    user = User.objects.get(pk=pk)
    pastor = Pastor.objects.create(user=user)
    pastor.save()
    context = {
         'message':'success'
     }
    return JsonResponse(context, safe=False)

def listofHous(request,pk ):
    dept = Department.objects.get(pk=pk)
    depts = Unit.objects.filter(department = dept)
    workers = Worker.objects.filter(approved=True)
    return render(request, 'department/hous.html', {'dept':depts, 'workers':workers})

def addHou(request, pk, worker):
    dept = Unit.objects.get(pk=pk)
    worker = Worker.objects.get(pk=worker)
    dept.hou = worker.user
    user = User.objects.get(id = dept.hou.pk)
    user.role ="HOU"
    user.save()
    dept.save()
    context = {
        'dept':dept.name,
        'username':dept.hou.username,
        'first_name':dept.hou.first_name,
        'last_name':dept.hou.last_name,
        'phone':dept.hou.phone,
    }
    return JsonResponse(context, safe=False)


def fillAcademy(request):
    if request.method == "POST":
        form = AcademicForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            form.save()
            return redirect('profile')
    else:
        form = AcademicForm()
    return render(request, 'department/formaca.html', {'form':form})
