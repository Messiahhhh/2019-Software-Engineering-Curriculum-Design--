from django.db import models
from django.db import models
from courseScheduling.models import Teacher_Schedule_result
# Create your models here.

from backstage.models import Teacher, Student, \
    College, MajorPlan, AdmClass, ClassRoom
from scoreManagement.models import Course, MajorCourses, Teaching


class CourseSelected(models.Model):
    sno = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    cno = models.ForeignKey(to=Teacher_Schedule_result, on_delete=models.CASCADE)
    score = models.FloatField()
    common_score = models.FloatField(null=True)
    final_score = models.FloatField(null=True)

    class Meta:
        db_table = "course_selected"


class Picture(models.Model):
    pic = models.ImageField(upload_to='static/img/adm_query')

    def __str__(self):
        return self.pic


class BEGIN_AND_END_TIME:
    begin_time = models.ForeignKey(to=AdmClass, on_delete=models.CASCADE)
    end_time = models.ForeignKey(to=AdmClass, on_delete=models.CASCADE)

    def __str__(self):
        return self.begin_time + '-->' + self.end_time

    class Meta:
        db_table = "time"
