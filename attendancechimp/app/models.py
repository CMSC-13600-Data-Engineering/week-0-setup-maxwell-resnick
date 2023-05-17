from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#this class records data on the course ID and the name of the course
class Course(models.Model):
    course_id = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    meeting_time = models.TimeField()
    times_per_week = models.FloatField()
    instructor_id = models.CharField(max_length = 100)

#this class records data on whether the user is an instructor or student
class ACUser(models.Model):
    USER_TYPES = [
        ('Instructor', 'Instructor'),
        ('Student', 'Student'),
        ]
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    #name = models.CharField(max_length=100)
    #user_id = models.CharField(max_length=100)
    #email = models.EmailField(max_length=100)
    #password = models.CharField(max_length=100)
    djuser = models.ForeignKey(User, on_delete=models.CASCADE)

#this class maps user and course
class Enrollment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

#this class records data on the instructor, instructor's QR code, and time of generation
class Instructor_QR(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor_id = models.CharField(max_length=100)  
    instructor_qr = models.ImageField(upload_to ='uploads/')
    class_code = models.CharField(max_length=100)
    generation_time = models.TimeField() 

class Student_QR(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=100) 
    student_qr = models.FileField(upload_to ='uploads/')
    upload_time = models.TimeField()  

import logging

def newUser(name, email, user_type, password):
    if User.objects.filter(email=email).count() > 0:
        raise ValueError('This email is already in use!')
    
    new_djuser = User(first_name=name, username=email, email=email, password=password)
    new_djuser.save()

    new_user = ACUser(djuser=new_djuser,user_type=user_type)
    new_user.save()
    #logging.info('Added a new user ' + str((name, user_id, email, user_type, password)))

    return new_djuser

### Is this right?

def createCourse(course_name, course_id, start_date, end_date, meeting_time, times_per_week, instructor_id):
    if Course.objects.filter(course_id=course_id).count() > 0:
        raise ValueError('This Course ID is already in use!')
    if Course.objects.filter(instructor_id=instructor_id,meeting_time=meeting_time).count() > 0:
        raise ValueError('This instructor is already teaching a course at this time!')
    #if Course.end_date <= Course.start_date:
    #    raise ValueError("End date must be after start date!")
    new_course = Course(course_name=course_name, course_id=course_id, start_date=start_date, end_date=end_date, meeting_time=meeting_time, times_per_week=times_per_week)
    new_course.save()


def joinCourse(course_name, course_id):
    new_join = Course(course_name=course_name, course_id=course_id)
    new_join.save()


from datetime import datetime
def trackAttendance(class_code, generation_time):
    new_attendance = Instructor_QR(class_code=class_code, generation_time=datetime.now())
    new_attendance.save()


def uploadQR(student_qr):
    new_upload = Student_QR(student_qr=student_qr)
    new_upload.save()
