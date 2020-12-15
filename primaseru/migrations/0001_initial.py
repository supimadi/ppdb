# Generated by Django 3.1.4 on 2020-12-15 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CityList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100, verbose_name='Nama Kota')),
            ],
        ),
        migrations.CreateModel(
            name='ProvinceList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_name', models.CharField(max_length=100, verbose_name='Nama Provinsi')),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_regis', models.PositiveIntegerField(verbose_name='No. Register')),
                ('sex', models.CharField(choices=[(None, '=Pilih='), ('L', 'Laki - Laki'), ('P', 'Perempuan')], max_length=1, verbose_name='Jenis Kelamin')),
                ('nisn', models.PositiveIntegerField(verbose_name='NISN')),
                ('date_born', models.DateField(verbose_name='Tanggal Lahir')),
                ('nik', models.PositiveIntegerField(unique=True, verbose_name='Nomor Induk Kependudukan (NIK)')),
                ('no_kk', models.PositiveIntegerField(verbose_name='Nomor Kartu Keluarga (KK)')),
                ('religion', models.CharField(choices=[(None, '=Pilih='), ('ISL', 'Islam'), ('KRS', 'Kristen'), ('KTL', 'Katolik'), ('HND', 'Hindu'), ('BDH', 'Budha'), ('KHC', 'Kong Hu Cu')], max_length=3, verbose_name='Agama')),
                ('address_kk', models.TextField(verbose_name='Alamat KK')),
                ('kecamatan', models.CharField(max_length=120)),
                ('kelurahan', models.CharField(max_length=120)),
                ('dusun', models.CharField(max_length=120)),
                ('rt_rw', models.CharField(max_length=8, verbose_name='RT/RW')),
                ('real_address', models.TextField(verbose_name='Alamat Sekarang')),
                ('resident', models.CharField(max_length=50, verbose_name='Tempat Tinggal')),
                ('transport', models.CharField(max_length=50, verbose_name='Alat Transportasi')),
                ('handpone', models.PositiveIntegerField(verbose_name='No. HP')),
                ('email', models.EmailField(max_length=254)),
                ('social_media', models.CharField(max_length=100, verbose_name='Akun Sosial Media')),
                ('school_origin', models.CharField(max_length=120, verbose_name='Asal Sekolah')),
                ('npsn_school_origin', models.PositiveIntegerField(verbose_name='Nomor NPSN Sekolah Asal')),
                ('medic_record', models.TextField(blank=True, null=True, verbose_name='Riwayat Kesehatan')),
                ('blood_type', models.CharField(choices=[(None, '=Pilih='), ('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O'), ('0', 'Tidak Tahu')], max_length=2, verbose_name='Golongan Darah')),
                ('in_medicine', models.CharField(blank=True, max_length=120, null=True, verbose_name='Dalam Pengobatan')),
                ('private_doctor', models.CharField(blank=True, max_length=120, null=True, verbose_name='Nama Dokter Keluarga')),
                ('phone_doctor', models.PositiveIntegerField(blank=True, null=True, verbose_name='No Telepon Doktor')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='primaseru.citylist', verbose_name='Kota')),
                ('city_born', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='city_born', to='primaseru.citylist', verbose_name='Kota Kelahiran')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='primaseru.provincelist', verbose_name='Provinsi')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentGuardianProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120, verbose_name='Nama Lengkap')),
                ('date_born', models.DateField(verbose_name='Tanggal Lahir Wali')),
                ('nik', models.PositiveIntegerField(unique=True, verbose_name='Nomor Induk Kependudukan (NIK) Wali')),
                ('education', models.CharField(choices=[(None, '=Pilih='), ('SD', 'SD'), ('SLTP', 'SLTP'), ('SLTA', 'SLTA'), ('D2', 'D2'), ('D3', 'D3'), ('D4', 'D4'), ('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3')], max_length=4, verbose_name='Pendidikan Terakhir Wali')),
                ('job', models.CharField(blank=True, max_length=100, null=True, verbose_name='Pekerjaan Wali')),
                ('salary', models.PositiveIntegerField(blank=True, null=True, verbose_name='Penghasilan Wali')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email Wali')),
                ('phone', models.PositiveIntegerField(verbose_name='No. HP Wali')),
                ('child', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('city_born', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='primaseru.citylist', verbose_name='Kota Kelahiran Wali')),
            ],
        ),
        migrations.CreateModel(
            name='MotherStudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120, verbose_name='Nama Lengkap')),
                ('date_born', models.DateField(verbose_name='Tanggal Lahir Ibu')),
                ('nik', models.PositiveIntegerField(unique=True, verbose_name='Nomor Induk Kependudukan (NIK) Ibu')),
                ('education', models.CharField(choices=[(None, '=Pilih='), ('SD', 'SD'), ('SLTP', 'SLTP'), ('SLTA', 'SLTA'), ('D2', 'D2'), ('D3', 'D3'), ('D4', 'D4'), ('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3')], max_length=4, verbose_name='Pendidikan Terakhir Ibu')),
                ('job', models.CharField(blank=True, max_length=100, null=True, verbose_name='Pekerjaan Ibu')),
                ('salary', models.PositiveIntegerField(blank=True, null=True, verbose_name='Penghasilan Ibu')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email Ibu')),
                ('phone', models.PositiveIntegerField(verbose_name='No. HP Ibu')),
                ('child', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('city_born', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='primaseru.citylist', verbose_name='Kota Kelahiran Ibu')),
            ],
        ),
        migrations.CreateModel(
            name='MajorStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_major', models.CharField(choices=[(None, '=Pilih='), ('TKJ', 'Teknik Komputer dan Jaringan'), ('TJAT', 'Teknik Jaringan Akses dan Telekomunikasi'), ('MM', 'Multimedia')], max_length=4, verbose_name='Pilihan Jurusan Pertama')),
                ('second_major', models.CharField(choices=[(None, '=Pilih='), ('TKJ', 'Teknik Komputer dan Jaringan'), ('TJAT', 'Teknik Jaringan Akses dan Telekomunikasi'), ('MM', 'Multimedia')], max_length=4, verbose_name='Pilihan Jurusan Kedua')),
                ('info', models.CharField(max_length=120, verbose_name='Info Primaseru (PPDB)')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FatherStudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120, verbose_name='Nama Lengkap')),
                ('date_born', models.DateField(verbose_name='Tanggal Lahir Ayah')),
                ('nik', models.PositiveIntegerField(unique=True, verbose_name='Nomor Induk Kependudukan (NIK) Ayah')),
                ('education', models.CharField(choices=[(None, '=Pilih='), ('SD', 'SD'), ('SLTP', 'SLTP'), ('SLTA', 'SLTA'), ('D2', 'D2'), ('D3', 'D3'), ('D4', 'D4'), ('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3')], max_length=4, verbose_name='Pendidikan Terakhir Ayah')),
                ('job', models.CharField(blank=True, max_length=100, null=True, verbose_name='Pekerjaan Ayah')),
                ('salary', models.PositiveIntegerField(blank=True, null=True, verbose_name='Penghasilan Ayah')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email Ayah')),
                ('phone', models.PositiveIntegerField(verbose_name='No. HP Ayah')),
                ('child', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('city_born', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='primaseru.citylist', verbose_name='Kota Kelahiran Ayah')),
            ],
        ),
        migrations.AddField(
            model_name='citylist',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='primaseru.provincelist'),
        ),
    ]
