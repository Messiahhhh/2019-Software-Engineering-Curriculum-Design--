from django.db import models
<<<<<<< HEAD
from django.db import models

# Create your models here.

from backstage.models import Teacher, Student,\
    College, MajorPlan, AdmClass, ClassRoom
from scoreManagement.models import Course,MajorCourses,Teaching

class courseSelected(models.Model):
    sno = models.ForeignKey(to=Student,on_delete=models.CASCADE)
    course = models.ForeignKey(to=MajorCourses,on_delete=models.CASCADE)
    tno = models.ForeignKey(to=Teacher,on_delete=models.CASCADE)
    time = models.CharField(max_length=20)
    classroom = models.CharField(max_length=20)
    score = models.FloatField()

class TeachersCourse(models.Model):
    tno = models.ForeignKey(to=Teacher,on_delete=models.CASCADE)
    course = models.ForeignKey(to=MajorCourses,on_delete=models.CASCADE)
    stu_num = models.IntegerField()





=======
from backstage.models import Student, Teacher
from scoreManagement.models import Course, MajorCourses


>>>>>>> b12887070dca45507f23fcc57d4d880354fe094e
