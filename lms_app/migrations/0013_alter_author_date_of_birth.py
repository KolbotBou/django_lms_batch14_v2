# Generated by Django 4.2.16 on 2024-11-21 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0012_alter_author_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
