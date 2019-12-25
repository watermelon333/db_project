# Generated by Django 2.2.6 on 2019-12-21 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qqa', '0006_auto_20191221_1731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='age',
            new_name='student_age',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='student_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='sno',
            new_name='student_no',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='sex',
            new_name='student_sex',
        ),
        migrations.AlterField(
            model_name='studentcourse',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qqa.Student', to_field='student_no'),
        ),
    ]