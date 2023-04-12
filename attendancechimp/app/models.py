from django.db import models

# Create your models here.

#this class records data on the course ID and the name of the course
class Course(models.Model):
    course_id = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)

#this class records data on whether the user is an instructor or student
class User(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    USER_TYPES = [
        ('Instructor'),
        ('Student'),
        ]
    type_user = models.CharField(max_length=10, choices=USER_TYPES)

#this class records data on the instructor, instructor's QR code, and time of generation
class Instructor_QR(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor_name = models.CharField(max_length=100)  
    instructor_qr = models.ImageField(upload_to ='uploads/')
    generation_time = models.TimeField() 

class Student_QR(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100) 
    student_qr = models.ImageField(upload_to ='uploads/')
    upload_time = models.TimeField() 