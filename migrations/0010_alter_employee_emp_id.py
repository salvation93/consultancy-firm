# Generated by Django 3.2 on 2021-05-08 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0009_alter_employee_emp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp663', max_length=70),
        ),
    ]
