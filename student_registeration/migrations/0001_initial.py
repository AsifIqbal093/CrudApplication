# Generated by Django 3.1.6 on 2021-02-22 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_program', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_name', models.CharField(max_length=50)),
                ('std_fname', models.CharField(max_length=50)),
                ('std_phone', models.CharField(max_length=13)),
                ('std_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_registeration.programdetails')),
            ],
        ),
    ]
