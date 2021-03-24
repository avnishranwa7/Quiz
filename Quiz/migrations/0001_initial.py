# Generated by Django 3.1.7 on 2021-03-24 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('Course_ID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Course_Name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Student_data_insert',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('RollNo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Mail', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'students',
            },
        ),
        migrations.CreateModel(
            name='Teacher_data_insert',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('Teacher_ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Mail', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('quiz_id', models.AutoField(primary_key=True, serialize=False)),
                ('quiz_name', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('duration', models.IntegerField()),
                ('Course_ID', models.ForeignKey(db_column='Course_ID', on_delete=django.db.models.deletion.CASCADE, to='Quiz.course')),
            ],
            options={
                'verbose_name': 'Quizze',
                'db_table': 'Quiz',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('q_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=500)),
                ('opt1', models.CharField(max_length=100)),
                ('opt2', models.CharField(max_length=100)),
                ('opt3', models.CharField(max_length=100)),
                ('opt4', models.CharField(max_length=100)),
                ('ans', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('quiz_id', models.ForeignKey(db_column='quiz_id', on_delete=django.db.models.deletion.CASCADE, to='Quiz.quiz')),
            ],
            options={
                'verbose_name': 'Question',
                'db_table': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='enrolled',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Course_ID', models.ForeignKey(db_column='Course_ID', on_delete=django.db.models.deletion.CASCADE, to='Quiz.course')),
                ('RollNo', models.ForeignKey(db_column='RollNo', on_delete=django.db.models.deletion.CASCADE, to='Quiz.student_data_insert')),
            ],
            options={
                'verbose_name': 'Enrolled Student',
                'db_table': 'enrolled',
            },
        ),
    ]
