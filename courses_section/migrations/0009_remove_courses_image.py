# Generated by Django 4.2.2 on 2023-07-03 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses_section', '0008_alter_courses_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='image',
        ),
    ]
