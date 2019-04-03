from django.db import models

# Create your models here.
class Student(models.Model):  # 学生表
    gender = (  # 性别选择
        ('male', '男'),
        ('female', '女'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')  # 一对一关联到User，定义关联名为student
    code = models.CharField(max_length=128, unique=True, default='201600000')  # 定义学生学号
    name = models.CharField(max_length=128, unique=False)  # 定义学生姓名
    sex = models.CharField(max_length=32, choices=gender, default='男')  # 定义学生性别
    age = models.CharField(max_length=128, unique=False)  # 定义学生年龄
    start_year = models.CharField(max_length=32, default='2019')  # 定义入学年
    length = models.CharField(max_length=128, unique=False)  # 定义学制
    major = models.ForeignKey("Major", on_delete=models.CASCADE, default=1)  # 外键关联主修
    department = models.ForeignKey("Dept", on_delete=models.CASCADE, default=1)  # 外键部门
    mod_data = models.DateTimeField('Last modified', auto_now=True)


