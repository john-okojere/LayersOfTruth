from django.urls import path
from .views import registerSiloam, SiloamTag,siloamtags,siloamDashboard,emailContact,AttendancDetailList, search_attendance, createAttendance, AttendanceList, search_attendancelist, email_list, registeredlist, search_registeredlist, workerstags, WorkerAttendanceList, WorkerAttendanceDetailList, Worker_search_attendance,pastorstags, PastorAttendanceList, PastorAttendanceDetailList, specialstags, addspecialcard, SpecialAttendanceList, SpecialAttendanceDetailList

urlpatterns = [
    path('', registerSiloam, name="siloam"),
    path('siloam-tag/<int:pk>/', SiloamTag, name="siloam-tag"),
    path('siloam-tags/', siloamtags, name="siloam-tags"),
    path('workers-tags/', workerstags, name="workers-tags"),
    path('pastor-tags/', pastorstags, name="pastor-tags"),
    path('special-tags/', specialstags, name="special-tags"),
    path('special-tags-form/', addspecialcard, name="special-tags-form"),

    path('Dashboard/', siloamDashboard, name="siloam-dashboard"),
    path('Dashboard/contacts', email_list, name="siloam-email-list"),
    path('Dashboard/registered', registeredlist, name="siloam-registered-list"),
    
    path('WorkerAttendance-detail-list/<int:pk>', WorkerAttendanceDetailList, name="workers-attendance-detail-list"),
    path('WorkerAttendance-list/', WorkerAttendanceList, name="workers-attendance-list"),
    
    
    path('SpecialAttendance-detail-list/<int:pk>', SpecialAttendanceDetailList, name="Specials-attendance-detail-list"),
    path('SpecialAttendance-list/', SpecialAttendanceList, name="Specials-attendance-list"),
    
    
    path('PastorAttendance-detail-list/<int:pk>', PastorAttendanceDetailList, name="Pastors-attendance-detail-list"),
    path('PastorAttendance-list/', PastorAttendanceList, name="Pastors-attendance-list"),
    

    path('Attendance-detail-list/<int:pk>', AttendancDetailList, name="siloam-attendance-detail-list"),
    path('Attendance-list/', AttendanceList, name="siloam-attendance-list"),
    path('email/', emailContact, name="siloam-subscribe"),
    path('create-attendance/', createAttendance, name="create-Attendance"),
    path('attendance/search/<str:name>', search_attendancelist, name="attendance-search"),
    path('attendance/search-worker/<str:name>', Worker_search_attendance, name="worker_attendance-search"),
    path('search/<str:name>', search_attendance, name="siloam-search"),
    path('search-register/<str:name>', search_registeredlist, name="siloam-register-search"),
]

