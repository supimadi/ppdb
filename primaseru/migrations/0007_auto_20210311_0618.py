# Generated by Django 3.1.4 on 2021-03-11 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primaseru', '0006_auto_20210310_0813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='accepted',
        ),
        migrations.AlterField(
            model_name='fatherstudentprofile',
            name='full_name',
            field=models.CharField(db_index=True, max_length=120, verbose_name='Nama Lengkap'),
        ),
        migrations.AlterField(
            model_name='fatherstudentprofile',
            name='verified',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='majorstudent',
            name='verified',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='motherstudentprofile',
            name='full_name',
            field=models.CharField(db_index=True, max_length=120, verbose_name='Nama Lengkap'),
        ),
        migrations.AlterField(
            model_name='motherstudentprofile',
            name='verified',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='studentfile',
            name='verified',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='studentguardianprofile',
            name='full_name',
            field=models.CharField(db_index=True, max_length=120, verbose_name='Nama Lengkap'),
        ),
        migrations.AlterField(
            model_name='studentguardianprofile',
            name='verified',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='verified',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]
