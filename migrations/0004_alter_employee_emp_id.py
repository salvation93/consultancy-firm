# Generated by Django 3.2 on 2021-05-08 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0003_alter_employee_emp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp520', max_length=70),
        ),
    ]
