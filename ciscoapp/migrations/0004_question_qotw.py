# Generated by Django 2.1.3 on 2019-01-04 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciscoapp', '0003_remove_question_qotw'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='qotw',
            field=models.CharField(db_column='qotw', default='n', max_length=1),
        ),
    ]