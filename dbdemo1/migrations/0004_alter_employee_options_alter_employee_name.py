# Generated by Django 4.2.2 on 2023-07-03 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbdemo1', '0003_alter_employee_options_alter_employee_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name_plural': 'Employees'},
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=10),
        ),
    ]
