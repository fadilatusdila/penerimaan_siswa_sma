from django import forms
from .models import Siswa, OrangTua

class PendaftaranForm(forms.Form):
    nama_siswa = forms.CharField(label='Nama Siswa')
    jenis_kelamin = forms.ChoiceField(choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')])
    tanggal_lahir = forms.DateField(label='Tanggal Lahir', widget=forms.DateInput(attrs={'type': 'date'}))
    asal_sekolah = forms.CharField(label='Asal Sekolah')

    nama_ayah = forms.CharField(label='Nama Ayah')
    pekerjaan_ayah = forms.CharField(label='Pekerjaan Ayah')
    nama_ibu = forms.CharField(label='Nama Ibu')
    pekerjaan_ibu = forms.CharField(label='Pekerjaan Ibu')
    alamat = forms.CharField(label='Alamat', widget=forms.Textarea)
