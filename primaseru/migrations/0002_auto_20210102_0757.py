# Generated by Django 3.1.4 on 2021-01-02 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('primaseru', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fatherstudentprofile',
            old_name='child',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='motherstudentprofile',
            old_name='child',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='studentguardianprofile',
            old_name='child',
            new_name='student',
        ),
    ]