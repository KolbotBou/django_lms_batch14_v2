# Generated by Django 4.2.16 on 2024-10-13 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0003_alter_book_isbn'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['id']},
        ),
    ]
