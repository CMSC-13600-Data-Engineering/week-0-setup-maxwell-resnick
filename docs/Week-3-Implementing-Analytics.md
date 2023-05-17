# 3. Data Analytics
This week you will be querying the data in the database to build a basic analytics dashboard for this application. Again, let's not worry about verifying the QR codes just yet (that's next week's project).

## Step 1. The `/app/overview?course=xyz` View
An instructor can visit the `/app/overview?course=xyz`, this should load summary statistics about class attendance for the course associated with the code `xyz`. This view should only load if the user is logged in and they are an instructor. If not logged in, redirect the user too the login view `/accounts/login`.

These summary statistics should have:
1. The class name/number printed at the top
2. The total number of students in the class
3. For each class meeting, you should have the fraction of students with any image uploaded.
 
## Step 2. The `/app/student?course=xyz` View
An instructor can visit the `/app/student?course=xyz`, this should load specific stats for a student in a course code `xyz`. This view should only load if the user is logged in and they are an instructor. If not logged in, redirect the user too the login view `/accounts/login`.

These statistics should have:
1. The class name/number printed at the top
2. For each class meeting, whether the student has an uploaded image or not.

## Step 3. Testing Plan (Write Below)
As you add more functionality to the application, testing becomes much harder. Write a detailed plan on how you are testing all of this functionality.

Hint: think about how to write scripts that generate fake data to add to the database.


Plan for testing: Our tests.py file will include a series of test cases. It will begin with the UserTests class, which will focus on testing user creation. We will generate fake data through the faker library, and in this case, we will create new users. We will verify that users are not "None" and that their attributes line up correctly with the generated data. The CourseTests class will test the creation of a course. Once again, fake data will be generated for course details, and the createCourse function will be used to create a course. The test will retrieve the course from the database and ensure it is not "None", while also verifying that the course's attributes align with the generated data. In the EnrollmentTests class, we will test the enrollment count for a course. We will set up three users (an instructor and two students) and a course using the setUp method. The test will then retrieve the enrollments for the course and check that the count matches the expected value. Lastly, the InstructorQRTests class will focus on testing the creation of an instructor QR record. It will set up a course and an instructor QR record and retrieve the instructor QR record from the database, ensuring once again that it is not "None".

## Step 4. Implement (Step 3)
Implement Step 3 in code and include the results with your submitted pull request. 