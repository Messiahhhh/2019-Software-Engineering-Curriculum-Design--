from django.db import models
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





