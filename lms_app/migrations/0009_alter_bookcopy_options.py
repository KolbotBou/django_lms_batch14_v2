# Generated by Django 4.2.16 on 2024-11-10 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0008_alter_bookcopy_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookcopy',
            options={'ordering': ['due_back', 'imprint'], 'permissions': (('can_mark_returned', 'Set book as Returned'),)},
        ),
    ]
