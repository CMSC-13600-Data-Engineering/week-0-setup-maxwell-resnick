from django.test import TestCase

# Create your tests here.


from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date, time
from faker import Factory
from app.models import *

faker = Factory.create()

class UserTests(TestCase):
    def test_new_user_creation(self):
        name = faker.name()
        email = faker.email()
        user_type = 'Instructor'
        password = faker.password()

        user = newUser(name, email, user_type, password)

        self.assertIsNotNone(user)
        self.assertEqual(user.first_name, name)
        self.assertEqual(user.username, email)
        self.assertEqual(user.email, email)
        self.assertEqual(user.groups.first().name, user_type)


class CourseTests(TestCase):
    def test_create_course(self):
        course_name = faker.word()
        course_id = faker.uuid4()
        start_date = date.today()
        end_date = date.today()
        meeting_time = time(10, 30)
        times_per_week = 2
        instructor_id = faker.uuid4()

        createCourse(course_name, course_id, start_date, end_date, meeting_time, times_per_week, instructor_id)

        course = Course.objects.get(course_id=course_id)
        self.assertIsNotNone(course)
        self.assertEqual(course.course_name, course_name)
        self.assertEqual(course.start_date, start_date)
        self.assertEqual(course.end_date, end_date)
        self.assertEqual(course.meeting_time, meeting_time)
        self.assertEqual(course.times_per_week, times_per_week)
        self.assertEqual(course.instructor_id, instructor_id)


class EnrollmentTests(TestCase):
    def setUp(self):
        instructor = User.objects.create_user(username=faker.email(), password=faker.password())
        student1 = User.objects.create_user(username=faker.email(), password=faker.password())
        student2 = User.objects.create_user(username=faker.email(), password=faker.password())

        course = Course.objects.create(course_name=faker.word(), course_id=faker.uuid4())

        Enrollment.objects.create(user_id=instructor, course_id=course)
        Enrollment.objects.create(user_id=student1, course_id=course)
        Enrollment.objects.create(user_id=student2, course_id=course)

    def test_enrollment_count(self):
        course = Course.objects.first()
        enrollments = Enrollment.objects.filter(course_id=course)
        self.assertEqual(enrollments.count(), 3)


class InstructorQRTests(TestCase):
    def setUp(self):
        course = Course.objects.create(course_name=faker.word(), course_id=faker.uuid4())
        Instructor_QR.objects.create(course_id=course, instructor_id=faker.uuid4(), instructor_qr=faker.image_url(), class_code=faker.uuid4(), generation_time=timezone.now())

    def test_instructor_qr_creation(self):
        qr = Instructor_QR.objects.first()
        self.assertIsNotNone(qr)

