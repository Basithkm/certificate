# Generated by Django 4.1.4 on 2022-12-15 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_rename_birth_date_student_dob_remove_student_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='date_joined',
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
