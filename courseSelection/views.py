from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from backstage.models import Student, Teacher, College, Major, MajorPlan, ClassRoom, AdmClass
from scoreManagement.models import Course, MajorPlan, MajorCourses, CourseScore, Teaching
from courseScheduling.models import Teacher_Schedule_result
from courseSelection.models import CourseSelected
import json
import numpy as np
from django.conf import settings
from .models import Picture
import MySQLdb
import matplotlib.pyplot as plt
import matplotlib


def welcome(request):
    return render(request, 'courseSelection/welcome.html')


def selection_home_page(request):
    if request.session['user_type'] == '学生':
        return render(request, 'courseSelection/student_selection_manage.html')
    elif request.session['user_type'] == '教师':
        return render(request, 'courseSelection/teacher_selection_manage.html')
    else:
        return render(request, 'courseSelection/adm_selection_manage.html')


def stu_tongshi(request):
    return render(request, "courseSelection/stu_tongshi.html")


def stu_major(request):
    majorC = Teacher_Schedule_result.objects.all()[:3]
    data = []
    dat = []
    haveChosen = {}

    #     # crno = models.CharField(max_length=128)
    #     # crtype = models.CharField(null=False, max_length=10)
    #     # contain_num = models.IntegerField()
    sno = request.session["username"]
    courseChosen = CourseSelected.objects.filter(sno__username=sno)
    for c in courseChosen:
        tmp = {}
        haveChosen[c.cno.id] = 1
        tmp["id"] = c.cno.id
        tmp["课程号"] = c.cno.tno.mcno.cno.cno
        tmp["课程名"] = c.cno.tno.mcno.cno.cname
        tmp["学时"] = c.cno.tno.mcno.hour_total
        tmp["选课人数"] = c.cno.current_number
        tmp["课程容量"] = c.cno.MAX_number
        tmp["授课教师"] = c.cno.tno.tno.name
        tmp["上课教室"] = c.cno.where.crno
        tmp["上课时间"] = c.cno.time
        dat.append(tmp)
    for major in majorC:
        tmp = {}
        try:
            if haveChosen[major.id] == 1:
                tmp["if_chosen"] = 1
        except:
            tmp["if_chosen"] = 0
        tmp["id"] = major.id
        tmp["课程号"] = major.tno.mcno.cno.cno
        tmp["课程名"] = major.tno.mcno.cno.cname
        tmp["学时"] = major.tno.mcno.hour_total
        tmp["选课人数"] = major.current_number
        tmp["课程容量"] = major.MAX_number
        tmp["授课教师"] = major.tno.tno.name
        tmp["上课教室"] = major.where.crno
        tmp["上课时间"] = major.time
        if tmp["选课人数"] < tmp["课程容量"]:
            data.append(tmp)
    return render(request, "courseSelection/stu_major.html", {'data': json.dumps(data), 'dat': json.dumps(dat)})


def select_course(request):
    if request.is_ajax():
        if request.method == 'GET':
            print("asdasd")
            flag = 1
            ID = request.GET.get("id")
            sno = request.session["username"]
            X = np.zeros((25, 8, 14), dtype=np.int)
            confilict_candidate = CourseSelected.objects.filter(sno__username=sno)  # 选的不同的课
            tot = 0
            course_time = []  # 收集这些课程的上课时间
            for i in confilict_candidate:
                tmp = i.cno.time.split(",")  # 同一门课程在一周内不同的时间上
                for j in tmp:  # 一周内不同的天
                    dic = {}
                    district = j.split("-")
                    dic["周数"] = district[2] + "-" + district[3]
                    dic["节次"] = district[0] + "-" + district[1]
                    course_time.append(dic)
            for i in course_time:
                week = i["周数"].split("-")
                times = i["节次"].split("-")
                cstart = 0
                cend = 0
                Day = 0
                if int(times[1]) >= 1 and int(times[1]) <= 13:
                    Day = 1
                elif int(times[1]) >= 14 and int(times[1]) <= 26:
                    Day = 2
                elif int(times[1]) >= 27 and int(times[1]) <= 39:
                    Day = 3
                elif int(times[1]) >= 40 and int(times[1]) <= 52:
                    Day = 4
                elif int(times[1]) >= 53 and int(times[1]) <= 65:
                    Day = 5
                elif int(times[1]) >= 66 and int(times[1]) <= 78:
                    Day = 6
                elif int(times[1]) >= 79 and int(times[1]) <= 91:
                    Day = 7

                cstart = int(times[0]) % 13
                cend = int(times[1]) % 13

                if cstart == 0:
                    cstart = 13
                if cend == 0:
                    cend = 13
                X[int(week[0]):int(week[1]) + 1, Day, cstart:cend + 1] = 1

            stu_new = Student.objects.get(username=sno)
            teach = Teacher_Schedule_result.objects.get(id=ID)
            tmp = teach.time.split(",")
            single_course = []
            if teach.current_number >= teach.MAX_number:
                flag = 3
                return JsonResponse(
                    {"flag": flag, "tot": tot})
            else:
                for j in tmp:
                    dic = {}
                    district = j.split("-")
                    dic["周数"] = district[2] + "-" + district[3]
                    dic["节次"] = district[0] + "-" + district[1]
                    single_course.append(dic)

                for j in single_course:
                    week = j["周数"].split("-")
                    times = j["节次"].split("-")
                    cstart = 0
                    cend = 0
                    Day = 0
                    if int(times[1]) >= 1 and int(times[1]) <= 13:
                        Day = 1
                    elif int(times[1]) >= 14 and int(times[1]) <= 26:
                        Day = 2
                    elif int(times[1]) >= 27 and int(times[1]) <= 39:
                        Day = 3
                    elif int(times[1]) >= 40 and int(times[1]) <= 52:
                        Day = 4
                    elif int(times[1]) >= 53 and int(times[1]) <= 65:
                        Day = 5
                    elif int(times[1]) >= 66 and int(times[1]) <= 78:
                        Day = 6
                    elif int(times[1]) >= 79 and int(times[1]) <= 91:
                        Day = 7

                    cstart = int(times[0]) % 13
                    cend = int(times[1]) % 13
                    if cstart == 0:
                        cstart = 13
                    if cend == 0:
                        cend = 13

                    if np.sum(X[int(week[0]):int(week[1]) + 1, Day, cstart:cend + 1]) != 0:
                        flag = 0
                        print(flag)
                        break

                if (flag):
                    new_cord = CourseSelected()
                    new_cord.sno = stu_new
                    new_cord.cno = teach
                    new_cord.score = 0
                    new_cord.save()
                    tot = teach.current_number
                    tot += 1
                    Teacher_Schedule_result.objects.filter(id=ID).update(current_number=tot)

                return JsonResponse(
                    {"flag": flag, "tot": tot})


def delete(request):
    if request.is_ajax():
        if request.method == 'GET':
            ID = request.GET.get("id")
            sno = request.session["username"]
            teach = Teacher_Schedule_result.objects.get(id=ID)

            tot = teach.current_number
            tot -= 1
            print(ID)
            Teacher_Schedule_result.objects.filter(id=ID).update(current_number=tot)
            X = CourseSelected.objects.filter(sno__username=sno, cno_id=ID)
            X.delete()

            return JsonResponse({"flag": 1, "tot": tot, "ID": ID})


def teacher(request):  # 教师查看授课选课情况
    return render(request, "courseSelection/index.html")


def find_course(request):
    if request.is_ajax():
        if request.method == 'GET':
            sno = request.session["username"]
            theCourse = CourseSelected.objects.filter(sno__username=sno)

            course_time = []  # 收集这些课程的上课时间
            dic = {}
            tmp = {}
            for i in theCourse:
                tmp = i.cno.time.split(",")  # 同一门课程在一周内不同的时间上
                dic[i.cno.tno.mcno.cno.cname] = []
                for j in tmp:  # 一周内不同的天
                    tmp = {}
                    district = j.split("-")
                    tmp["周数"] = district[2] + "-" + district[3]
                    tmp["节次"] = district[0] + "-" + district[1]
                    dic[i.cno.tno.mcno.cno.cname].append(tmp)
            return JsonResponse({"dic": dic})


def adm_selection_manage(request):
    return render(request, "courseSelection/adm_selection_manage.html")


def adm_class(request):
    return render(request, "courseSelection/adm_class.html")


def adm_school(request):
    return render(request, "courseSelection/adm_school.html")


def text(request):
    return render(request, "courseSelection/text.html")


def show_pic(request):
    pic_obj = Picture.objects.get(id=1)
    return


def school_query(request):
    print(132420198479292475)

    print("12312fdskjgcasuidgfwui")
    time = request.POST.get("time")
    grade = request.POST.get("grade")
    college = request.POST.get("college")
    subject = request.POST.get("subject")

    print(time, grade, college, subject)
    db = MySQLdb.connect("localhost", "root", "root", "ems", charset='utf8')
    cursor = db.cursor()

    # 使用execute方法执行SQL语句
    cursor.execute("SELECT * FROM course")

    # 使用 fetchone() 方法获取一条数据

    results = cursor.fetchall()
    n = 0
    # print(results)
    final_id = 0
    final_cno = 0
    final_cname = ""
    final_ctype = ""
    final_cscore = 0
    final_college = 0
    target = "CSE32500C"
    for row in results:
        id1 = row[0]
        cno = row[1]
        cname = row[2]
        typ = row[3]
        score = row[4]
        college = row[5]
        n += 1
        if cno == target:
            final_id = id1
            final_cno = cno
            final_cname = cname
            final_college = college
            final_cscore = score
            final_ctype = typ
            break

    cursor.execute("SELECT * FROM college")
    print(final_college)

    # cursor.execute("SELECT name,short_name FROM college WHERE id > %s",final_college)

    results = cursor.fetchall()
    # print(results)
    for row in results:
        id1 = row[0]
        if id1 == final_college:
            print(row[1], row[2])
            break
    # print(n)
    # print(final_cname)

    # 关闭数据库连接
    db.close()

    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False
    # plt.subplot(1, 3, 1)
    label_list = ["计科", "自动化", "电子信息"]  # 各部分标签
    size = [75, 35, 10]  # 各部分大小

    color = ["red", "green", "blue"]  # 各部分颜色
    explode = [0.05, 0, 0]  # 各部分突出值

    patches, l_text, p_text = plt.pie(size, explode=explode, colors=color, labels=label_list, labeldistance=1.1,
                                      autopct="%1.1f%%", shadow=False, startangle=90, pctdistance=0.6)
    plt.axis("equal")  # 设置横轴和纵轴大小相等，这样饼才是圆的
    plt.legend()
    # plt.show()
    # plt.savefig( 'C:/Users/Lenovo/Desktop/test/2019-Software-Engineering-Curriculum-Design-master/2019-Software-Engineering-Curriculum-Design-master/EMS/static/img/adm_query/test2.jpg')
    plt.figure()
    x = ["2016-2017", "2017-2018", "2018-2019"]
    y = [135, 166, 189]
    # plt.subplot(1, 3, 2)
    plt.plot(x, y)
    # plt.savefig('C:/Users/Lenovo/Desktop/test/2019-Software-Engineering-Curriculum-Design-master/2019-Software-Engineering-Curriculum-Design-master/EMS/static/img/adm_query/test1.jpg')
    plt.figure()
    # plt.subplot(1, 3, 3)
    plt.bar(label_list, size)
    # plt.savefig('C:/Users/Lenovo/Desktop/test/2019-Software-Engineering-Curriculum-Design-master/2019-Software-Engineering-Curriculum-Design-master/EMS/static/img/adm_query/test3.jpg')
    # plt.show()
    print(123245432456432)
    return render(request, "courseSelection/adm_showimg.html")


def class_query(request):
    time = request.POST.get("time")
    grade = request.POST.get("grade")
    college = request.POST.get("college")
    subject = request.POST.get("subject")
    print(time, grade, college, subject)
    return render(request, "courseSelection/adm_classshow.html")


def time_set(request):
    '''
    print(12334)
    if request.method == 'POST':
        print('sdas')

    if request.is_ajax():
        print(12324)
        if request.method == 'POST':
            print(323)

    print(request)
    '''
    begin = request.POST.get('begin_time')
    request.session['begin_time'] = begin
    end = request.POST.get('end_time')
    request.session['end_time'] = end
    print(request.session['begin_time'])
    print(1)
    print(request.session['end_time'])
    return render(request, "courseSelection/adm_selection_manage.html")
