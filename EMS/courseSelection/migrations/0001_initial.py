# Generated by Django 2.1 on 2019-05-03 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backstage', '0001_initial'),
        ('scoreManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='courseSelected',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_Schedule_result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crno', models.CharField(max_length=128)),
                ('crtype', models.CharField(max_length=10)),
                ('contain_num', models.IntegerField()),
                ('time', models.CharField(max_length=128)),
                ('current_number', models.IntegerField()),
                ('MAX_number', models.IntegerField()),
                ('state', models.CharField(max_length=128)),
                ('tno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoreManagement.Teaching')),
            ],
            options={
                'db_table': 'Teacher_Schedule_result',
            },
        ),
        migrations.AddField(
            model_name='courseselected',
            name='cno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseSelection.Teacher_Schedule_result'),
        ),
        migrations.AddField(
            model_name='courseselected',
            name='sno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.Student'),
        ),
        migrations.AlterUniqueTogether(
            name='teacher_schedule_result',
            unique_together={('tno', 'time')},
        ),
    ]