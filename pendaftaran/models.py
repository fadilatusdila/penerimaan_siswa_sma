from django.db import models

class Siswa(models.Model):
    nama = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(max_length=10)
    tanggal_lahir = models.DateField()
    asal_sekolah = models.CharField(max_length=100)

class OrangTua(models.Model):
    nama_ayah = models.CharField(max_length=100)
    pekerjaan_ayah = models.CharField(max_length=100)
    nama_ibu = models.CharField(max_length=100)
    pekerjaan_ibu = models.CharField(max_length=100)
    alamat = models.TextField()

class Pendaftaran(models.Model):
    siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    orang_tua = models.ForeignKey(OrangTua, on_delete=models.CASCADE)
    tanggal_pendaftaran = models.DateField(auto_now_add=True)

