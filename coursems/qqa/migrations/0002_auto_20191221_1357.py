# Generated by Django 3.0 on 2019-12-21 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qqa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=12)),
                ('sex', models.CharField(max_length=6)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'Student',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_no', models.AutoField(primary_key=True, serialize=False)),
                ('teacher_name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=2)),
                ('title', models.CharField(choices=[('Instructor', '讲师'), ('Assitant', '助理教授'), ('Associate', '副教授'), ('Professor', '教授')], default='Instructor', max_length=15)),
            ],
            options={
                'db_table': 'Teacher',
            },
        ),
        migrations.CreateModel(
            name='TC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qqa.Course')),
                ('teacher_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qqa.Teacher')),
            ],
            options={
                'db_table': 'TC',
            },
        ),
        migrations.CreateModel(
            name='SC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=15, verbose_name='学期')),
                ('score', models.IntegerField(blank=True, null=True, verbose_name='成绩')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qqa.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qqa.Student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qqa.Teacher')),
            ],
            options={
                'db_table': 'SC',
            },
        ),
    ]