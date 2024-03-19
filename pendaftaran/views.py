from django.shortcuts import render
from .forms import PendaftaranForm

def pendaftaran(request):
    if request.method == 'POST':
        form = PendaftaranForm(request.POST)
        if form.is_valid():
            return render(request, 'pendaftaran/pendaftaran_berhasil.html')
    else:
        form = PendaftaranForm()
    return render(request, 'pendaftaran/pendaftaran.html', {'form': form})
