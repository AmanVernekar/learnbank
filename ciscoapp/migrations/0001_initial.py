# Generated by Django 2.1.3 on 2018-11-25 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.CharField(db_column='email_id', max_length=50)),
                ('password', models.CharField(db_column='password', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'logins',
                'db_table': 'login',
            },
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('subject', models.CharField(db_column='subject', max_length=80, primary_key=True, serialize=False)),
                ('chapter', models.CharField(db_column='chapter', max_length=80)),
                ('question', models.CharField(db_column='question', max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'questions',
                'db_table': 'question',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll_nbr', models.IntegerField(db_column='roll_nbr', default=0, primary_key=True, serialize=False)),
                ('student_name', models.CharField(db_column='student_name', max_length=30)),
                ('subject', models.CharField(max_length=20)),
                ('standard', models.IntegerField(db_column='standard', default=0)),
            ],
            options={
                'verbose_name_plural': 'students',
                'db_table': 'students',
            },
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(db_column='sub', max_length=50)),
                ('chp', models.CharField(db_column='chp', max_length=25, null=True)),
            ],
            options={
                'verbose_name_plural': 'subjects',
                'db_table': 'subject',
            },
        ),
    ]
