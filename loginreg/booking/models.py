from django.db import models
from django.contrib.auth.models import User

# from loginreg import booking

# Create your models here.
class Subject(models.Model):
    class_number = models.CharField(max_length=5, default="")
    subject_name = models.CharField(max_length=64, default="")
    section = models.CharField(max_length=10, default="")
    semester = models.CharField(max_length=10, default="")
    year = models.CharField(max_length=10, default="")
    seatss = models.CharField(max_length=10, default="")

    def __str__(self):
        return f"{self.class_number} {self.subject_name} {self.section} {self.semester} {self.year} {self.seatss}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    course_number = models.ForeignKey(Subject, on_delete=models.CASCADE, default="")
    
    def __str__(self):
        return f"{self.user} {self.course_number}"

##class ShowBooking(models.Model):
    ##show_me = models.CharField

#class Student(models.Model):
    ##first = models.CharField(max_length=64)
    ##last = models.CharField(max_length=64)
    ##booking = models.ManyToManyField(Booking, blank=True, related_name="student")

    ##def __str__(self):
        ##return f"{ self.first } { self.last }"