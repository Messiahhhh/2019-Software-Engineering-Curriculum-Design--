<<<<<<< HEAD
# Generated by Django 2.1 on 2019-04-19 15:35
=======
# Generated by Django 2.1.7 on 2019-04-20 09:43
>>>>>>> b12887070dca45507f23fcc57d4d880354fe094e

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backstage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cno', models.CharField(max_length=9)),
                ('cname', models.CharField(max_length=128)),
                ('course_type', models.CharField(max_length=128, null=True)),
                ('score', models.FloatField()),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.College')),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
<<<<<<< HEAD
=======
            name='CourseScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('sno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.Student')),
            ],
            options={
                'db_table': 'course_score',
            },
        ),
        migrations.CreateModel(
            name='EvaluationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item1', models.CharField(max_length=128)),
                ('item2', models.CharField(max_length=128)),
                ('item3', models.CharField(max_length=128)),
                ('item4', models.CharField(max_length=128)),
                ('item5', models.CharField(max_length=128)),
                ('item6', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('is_finish', models.BooleanField()),
            ],
            options={
                'db_table': 'evaluation_form',
            },
        ),
        migrations.CreateModel(
>>>>>>> b12887070dca45507f23fcc57d4d880354fe094e
            name='MajorCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour_total', models.IntegerField()),
                ('hour_class', models.IntegerField()),
                ('hour_other', models.IntegerField()),
                ('year', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('exam_method', models.BooleanField(default=True)),
                ('cno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoreManagement.Course')),
                ('mno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.MajorPlan')),
            ],
            options={
                'db_table': 'major_courses',
            },
        ),
        migrations.CreateModel(
            name='Teaching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
<<<<<<< HEAD
                ('mcno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoreManagement.MajorCourses')),
=======
                ('mcno', models.ManyToManyField(to='scoreManagement.MajorCourses')),
>>>>>>> b12887070dca45507f23fcc57d4d880354fe094e
                ('tno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.Teacher')),
            ],
            options={
                'db_table': 'teaching_table',
            },
        ),
<<<<<<< HEAD
=======
        migrations.AddField(
            model_name='evaluationform',
            name='teaching',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='scoreManagement.Teaching'),
        ),
        migrations.AddField(
            model_name='coursescore',
            name='teaching',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='scoreManagement.Teaching'),
        ),
>>>>>>> b12887070dca45507f23fcc57d4d880354fe094e
        migrations.AlterUniqueTogether(
            name='majorcourses',
            unique_together={('cno', 'mno', 'year', 'semester')},
        ),
    ]
