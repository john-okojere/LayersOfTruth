
from django.urls import path, re_path
from .views import departmentDashboard, createDepartment, departmentview, unitview, unitDashboard, createunit, workersform, getunits, joinDept,workerslist, deptworkerlist,pendingworkerslist, search_worker, asearch_worker, approveworker, approvedworkerslist, createTask, ListTask,unitmember, listofHod, addHou, listofHous, addHod, listofPastors, addPastor, fillAcademy
urlpatterns = [
    path('Dashboard/', departmentDashboard, name="department-dashboard"),
    path('create/', createDepartment,name="create-department"),
    path('<int:pk>/', departmentview,name="view-department"),

     path('<int:pk>/unit/Dashboard/', unitDashboard, name="unit-dashboard"),
    path('<int:pk>/unit/create/', createunit,name="create-unit"),
    path('<int:pk>/unit/<int:unit>/', unitview,name="view-unit"),

    path('apply-form/',workersform, name="workers-form"),
    path('workers/', workerslist,name="workerlist"),
    path('<int:pk>/workers/', deptworkerlist,name="dept-workerlist"),
    path('approved/<int:pk>/workers/', approveworker,name="approved-worker"),

    path('workers/search/<str:name>', search_worker,name="searchworkerlist"),
    path('workersapproved/search/<str:name>', asearch_worker,name="searchworkerlist"),
    path('workers/pending', pendingworkerslist,name="pendingworkerlist"),
    path('<int:pk>/workers/Approved/', approvedworkerslist,name="approvedworkerlist"),


    path('apply/',joinDept, name="workers-join"),
    path('<int:pk>/unit-list', getunits, name="getunits"),
    
    path('<int:unit>/create-unit-task', createTask, name="createtask"),
    path('<int:unit>/task_list/', ListTask, name="task_list"),
    path('<int:unit>/unit-member/',unitmember, name='unitmember'),

    path('hods/', listofHod, name="listofhods"),
    path('add/<int:pk>/hods/<int:worker>', addHod, name="addhods"),

    path('Pastors/', listofPastors, name="listofPastors"),
    path('add/<int:pk>/Pastors/', addPastor, name="addPastors"),


    path('<int:pk>/hous/', listofHous, name="listofhous"),
    path('add/<int:pk>/hous/<int:worker>', addHou, name="addhous"),
    
    path('academic-Form', fillAcademy, name="academyform")


]