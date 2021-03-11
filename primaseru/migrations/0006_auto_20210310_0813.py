# Generated by Django 3.1.4 on 2021-03-10 08:13

from django.db import migrations, models
import primaseru.models


class Migration(migrations.Migration):

    dependencies = [
        ('primaseru', '0005_registerschedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentfile',
            name='color_blind_cert',
            field=models.FileField(blank=True, null=True, upload_to=primaseru.models.user_directory_path, verbose_name='Semester Keterangan Tidak Buta Warna'),
        ),
        migrations.AlterField(
            model_name='studentfile',
            name='healty_cert',
            field=models.FileField(blank=True, null=True, upload_to=primaseru.models.user_directory_path, verbose_name='Surat Keterangan Sehat'),
        ),
        migrations.AlterField(
            model_name='studentfile',
            name='ra_sem_1',
            field=models.FileField(blank=True, null=True, upload_to=primaseru.models.user_directory_path, verbose_name='Rapor Semester 1'),
        ),
        migrations.AlterField(
            model_name='studentfile',
            name='ra_sem_2',
            field=models.FileField(blank=True, null=True, upload_to=primaseru.models.user_directory_path, verbose_name='Rapor Semester 2'),
        ),
        migrations.AlterField(
            model_name='studentfile',
            name='ra_sem_3',
            field=models.FileField(blank=True, null=True, upload_to=primaseru.models.user_directory_path, verbose_name='Rapor Semester 3'),
        ),
        migrations.AlterField(
            model_name='studentfile',
            name='ra_sem_4',
            field=models.FileField(blank=True, null=True, upload_to=primaseru.models.user_directory_path, verbose_name='Rapor Semester 4'),
        ),
    ]
