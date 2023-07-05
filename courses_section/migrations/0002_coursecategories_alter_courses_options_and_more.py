# Generated by Django 4.2.2 on 2023-07-03 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_section', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='courses',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelTable(
            name='courses',
            table='bignalytics_courses',
        ),
    ]
