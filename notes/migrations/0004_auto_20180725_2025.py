# Generated by Django 2.0.7 on 2018-07-25 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20180724_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note_text',
            field=models.TextField(max_length=1024),
        ),
    ]
