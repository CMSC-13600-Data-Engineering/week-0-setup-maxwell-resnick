from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('newUser', views.addUserForm, name='home'),
    path('handleUserForm', views.handleUserForm),

    path('createCourse', views.addCourseForm),
    path('handleCourseForm', views.handleCourseForm),
    
    path('joinCourse', views.joinCourseForm),
    path('join/', views.handleJoinForm, name='handle_join_form'),
    path('join/upload.html', views.handleUploadForm, name='upload_form'),
    path('handleJoinForm', views.handleJoinForm),

    path('uploadQR', views.newUploadForm),
    path('handleUploadForm', views.handleUploadForm),

    path('login', views.login_view),
    path('login_view', views.login_view),

    path('join/success.html', views.success_view),

    path('attendance', views.newAttendanceForm), 
    path('handleAttendanceForm', views.handleAttendanceForm),
    path('attendance/<str:course_id>/', views.handleAttendanceForm, name='attendance')
    #path('join/<str:course_id>/', views.join_course, name='join_course'),


]

#write a new path for new, create, etc