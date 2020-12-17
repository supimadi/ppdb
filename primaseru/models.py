from django.db import models
from users.models import CustomUser

from . import choices


class StudentProfile(models.Model):
    student = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    no_regis = models.PositiveIntegerField('No. Register')
    sex = models.CharField('Jenis Kelamin', max_length=1, choices=choices.SEX)
    nisn = models.PositiveIntegerField('NISN')
    city_born = models.CharField('Kota Kelahiran', max_length=100)
    date_born = models.DateField('Tanggal Lahir')
    nik = models.PositiveIntegerField('Nomor Induk Kependudukan (NIK)', unique=True)
    no_kk = models.PositiveIntegerField('Nomor Kartu Keluarga (KK)')
    religion = models.CharField('Agama', choices=choices.RELIGION, max_length=3)
    social_media = models.CharField('Akun Sosial Media', max_length=100)
    address_kk = models.TextField('Alamat KK')
    real_address = models.TextField('Alamat Sekarang')
    rt_rw = models.CharField('RT/RW', max_length=8)
    dusun = models.CharField(max_length=120)
    kelurahan = models.CharField(max_length=120)
    kecamatan = models.CharField(max_length=120)
    resident = models.CharField('Tempat Tinggal', max_length=50)
    transport = models.CharField('Alat Transportasi', max_length=50)
    handpone = models.PositiveIntegerField('No. HP')
    email = models.EmailField()
    school_origin = models.CharField('Asal Sekolah', max_length=120)
    npsn_school_origin = models.PositiveIntegerField('Nomor NPSN Sekolah Asal')
    medic_record = models.TextField('Riwayat Kesehatan', null=True, blank=True)
    blood_type = models.CharField('Golongan Darah', choices=choices.BLOOD_TYPE, max_length=2)
    in_medicine = models.CharField('Dalam Pengobatan', max_length=120)
    private_doctor = models.CharField('Nama Dokter Keluarga', max_length=120)
    phone_doctor = models.PositiveIntegerField('No Telepon Doktor')

    def __str__(self):
        return f'Profile {self.student}'


class FatherStudentProfile(models.Model):
    child = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField('Nama Lengkap', max_length=120)
    city_born = models.CharField('Kota Kelahiran Ayah', max_length=100)
    date_born = models.DateField('Tanggal Lahir Ayah')
    nik = models.PositiveIntegerField('Nomor Induk Kependudukan (NIK) Ayah', unique=True)
    education = models.CharField('Pendidikan Terakhir Ayah', max_length=4, choices=EDUCATION_LEVEL)
    job = models.CharField('Pekerjaan Ayah', max_length=100, null=True, blank=True)
    salary = models.PositiveIntegerField('Penghasilan Ayah', null=True, blank=True)
    email = models.EmailField('Email Ayah', null=True, blank=True)
    phone = models.PositiveIntegerField('No. HP Ayah')

    def __str__(self):
        return self.full_name

class MotherStudentProfile(models.Model):
    child = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField('Nama Lengkap', max_length=120)
    city_born = models.CharField('Kota Kelahiran Ibu', max_length=100)
    date_born = models.DateField('Tanggal Lahir Ibu')
    nik = models.PositiveIntegerField('Nomor Induk Kependudukan (NIK) Ibu', unique=True)
    education = models.CharField('Pendidikan Terakhir Ibu', max_length=4, choices=EDUCATION_LEVEL)
    job = models.CharField('Pekerjaan Ibu', max_length=100, null=True, blank=True)
    salary = models.PositiveIntegerField('Penghasilan Ibu', null=True, blank=True)
    email = models.EmailField('Email Ibu', null=True, blank=True)
    phone = models.PositiveIntegerField('No. HP Ibu')

    def __str__(self):
        return self.full_name

class StudentGuardianProfile(models.Model):
    child = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField('Nama Lengkap', max_length=120)
    city_born = models.CharField('Kota Kelahiran Wali', max_length=100)
    date_born = models.DateField('Tanggal Lahir Wali')
    nik = models.PositiveIntegerField('Nomor Induk Kependudukan (NIK) Wali', unique=True)
    education = models.CharField('Pendidikan Terakhir Wali', max_length=4, choices=EDUCATION_LEVEL)
    job = models.CharField('Pekerjaan Wali', max_length=100, null=True, blank=True)
    salary = models.PositiveIntegerField('Penghasilan Wali', null=True, blank=True)
    email = models.EmailField('Email Wali', null=True, blank=True)
    phone = models.PositiveIntegerField('No. HP Wali')

    def __str__(self):
        return self.full_name

class MajorStudent(models.Model):
    student = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_major = models.CharField('Pilihan Jurusan Pertama', choices=choices.MAJOR, max_length=4)
    second_major = models.CharField('Pilihan Jurusan Kedua', choices=choices.MAJOR, max_length=4)
    info = models.CharField('Info Primaseru (PPDB)', max_length=120)