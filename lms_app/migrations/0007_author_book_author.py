# Generated by Django 4.2.16 on 2024-10-13 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0006_alter_bookcopy_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text="Please Enter Author's First Name", max_length=200)),
                ('last_name', models.CharField(help_text="Please Enter Authos's Last Name", max_length=200)),
                ('date_of_birth', models.DateField()),
                ('date_of_death', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(help_text='Select a Author for the Book', null=True, on_delete=django.db.models.deletion.RESTRICT, to='lms_app.author'),
        ),
    ]
