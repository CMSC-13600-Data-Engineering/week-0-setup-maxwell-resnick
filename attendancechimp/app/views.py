from django.shortcuts import render
from django.http import HttpResponse
from app.models import newUser
from django.http import HttpResponseRedirect
from app.models import *
#### import all models


def index(request):
    return render(request, 'app/index.html', {"Illinois": "Chicago"})

## write in this file, addBook functions
## one add function, one handle function for each one

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def addUserForm(request, error_msg=''):
    return render(request, 'newUser.html', {'error': error_msg})

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

def handleUserForm(request):
        #First confirm that we have a POST request
    if request.method != "POST":
        return HttpResponse("Error: the request is not an HTTP POST request\n", status=500)


    #Second, let's log what this post request is doing
    print(str(request.POST))
    
    # if request.method == 'POST':
     #   name = request.POST['name']
      #  user_id = request.POST['user_id']
       # email = request.POST['email']
      #  user_type = request.POST['user_type']
       # password = request.POST['password']
    #try:
    name = request.POST['name']
    #user_id = request.POST['user_id']
    email = request.POST['email']
    user_type = request.POST['user_type']
    password = request.POST['password']

    user = newUser(name, email, user_type, password)

    login(request, user)
    if user_type == 'instructor':
        return render(request, 'createCourse.html')
    else:
        return render(request, 'success2.html')

def addCourseForm(request, error_msg=''):
    return render(request, 'createCourse.html', {'error': error_msg})

def handleCourseForm(request):
    if request.method != "POST":
        return HttpResponse("Error: the request is not an HTTP POST request\n", status=500)
    
    print(str(request.POST))

    #try
    course_name = request.POST['course_name']
    course_id = request.POST['course_id']
    start_date = request.POST['start_date']
    end_date = request.POST['end_date']
    meeting_time = request.POST['meeting_time']
    times_per_week = request.POST['times_per_week']
    instructor_id = request.POST['instructor_id']
    #except:
     #   return addCourseForm(request, error_msg='Please fill out all the fields of the form')

    #try:
    createCourse(course_name, course_id, start_date, end_date, meeting_time, times_per_week, instructor_id)
    return render(request, 'success.html')
    #except Exception as e:
    #    return addCourseForm(request, error_msg="Error: There is a database error in adding this course: " + str(e))



def joinCourseForm(request, error_msg=''):
    return render(request, 'join.html', {'error': error_msg})
    
from django.shortcuts import render, redirect
from .models import Course

def handleJoinForm(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')

        # Retrieve the course based on the provided course ID
        try:
            course_name = Course.objects.get(course_id=course_id)
        except Course.DoesNotExist:
            return render(request, 'join.html', {'error_message': 'Course does not exist.'})

        # Perform the logic to associate the student with the course
        # ...

        # Redirect to the success page
        return redirect('upload.html')  # Replace 'join_success' with the URL name for the join success page

    else:
        return render(request, 'join.html', {'error_message': 'Course does not exist.'})


def newUploadForm(request, error_msg=''):
    return render(request, 'upload.html', {'error': error_msg})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from app.models import Course, ACUser

from django.shortcuts import render, redirect

def handleUploadForm(request):
    return render(request, 'success3.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        objective = request.POST.get('objective')
        course_id = request.POST.get('course_id')

        if objective == 'join':
            return render(request, 'join.html')
        elif objective == 'upload':
            return render(request, 'upload.html')
        elif objective == 'class_summary':
            return render(request, 'class_summary.html')
        else:
            return render(request, 'attendance.html')
    else:
        return render(request, 'login.html')



        # Authenticate the user with the provided credentials
        #user = authenticate(request, username=username, password=password)

        #if user is not None:
            # Check if the user is a student
         #   if user.groups.filter(user_type='student').exists():
                # Log in the student
          #      login(request, user)
           #     return redirect('join.html')  # Replace 'student_dashboard' with the URL name for the student dashboard

            # Check if the user is an instructor
            #if user.groups.filter(name='Instructor').exists():
                # Log in the instructor
             #   login(request, user)
              #  return redirect('instructor_dashboard')  # Replace 'instructor_dashboard' with the URL name for the instructor dashboard

        # Invalid credentials or user is not a student/instructor
        #return render(request, 'login.html', {'error_message': 'Invalid username or password'})


#def handleUploadForm(request):
 #   if request.method != "POST":
  #      return HttpResponse("Error: the request is not an HTTP POST request\n", status=500)
   # if

    #try:
    #    course_name = request.POST['course_name']
    #    course_id = request.POST['course_id']
    #    joinCourse(course_name, course_id)
    #except Exception as e:
    #    return joinCourseForm(request, error_msg="Error: There is a database error in adding this course: " + str(e))

    #return joinCourseForm(request)

def success_view(request):
    return render(request, 'success3.html')


def newAttendanceForm(request, error_msg=''):
    return render(request, 'attendance.html', {'error': error_msg})

import random
import string
from django.shortcuts import render, get_object_or_404
from datetime import datetime

def handleAttendanceForm(request):
    # Generate a random class code
    class_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    # Store class_code and time_generated in the InstructorQR model
    qr_code = Instructor_QR(class_code=class_code, time_generated=datetime.now())
    qr_code.save()

    # Pass class_code to the template
    context = {'class_code': class_code}

    return render(request, 'attendance.html', context)

    return render(request, 'attendance.html', context)

def class_summary(request):
    # Get the class object
    course_obj = Enrollment.objects.get(course_id=course_id)
    
    # Get all the students in the class
    students = Enrollment.objects.filter(course=course_obj)
    
    # Get the total number of students in the class
    total_students = students.count()
    
    # Get all the meetings for the class
    meetings = Instructor_QR.objects.filter(course=course_obj).values('generation_time').annotate(total=Count('generation_time'))
    
    meeting_stats = []
    for meeting in meetings:
        # Get the number of students with images uploaded for the meeting
        students_with_images = Student_QR.filter(image__isnull=False, meeting=meeting).count()
        
        # Calculate the fraction of students with images uploaded for the meeting
        fraction_with_images = students_with_images / total_students if total_students > 0 else 0
        
        # Add meeting statistics to the list
        meeting_stats.append({
            'meeting_date': meeting.date,
            'fraction_with_images': fraction_with_images
        })
    
    context = {
        'class_name': class_obj.name,
        'total_students': total_students,
        'meeting_stats': meeting_stats
    }
    
    return render(request, 'class_summary.html', context)


def student_stats(request):
    course_id = request.GET.get('course_id')
    course = get_object_or_404(Course, code=course_id)

    class_meetings = Instructor_QR.objects.filter(course=course_id).values('generation_time').annotate(total=Count('generation_time'))
    students = Enrollment.objects.filter(course=course_id)

    student_stats = []
    for student in students:
        meeting_stats = []
        for meeting in class_meetings:
            has_uploaded_image = Student_QR.objects.filter(student=student_id, class_meeting=meeting).exists()
            meeting_stats.append({
                'meeting': meeting,
                'has_uploaded_image': has_uploaded_image
            })

        student_stats.append({
            'student': student,
            'meeting_stats': meeting_stats
        })

    context = {
        'course': course,
        'student_stats': student_stats
    }

    return render(request, 'student_stats.html', context)
