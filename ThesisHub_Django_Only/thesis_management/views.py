from django.shortcuts import render
from sinhvien.models import SinhVien
from detai.models import DeTai
from dangky.models import DangKy


def dashboard(request):
    tong_sv = SinhVien.objects.count()
    tong_dt = DeTai.objects.count()
    tong_dk = DangKy.objects.count()
    da_co_diem = DangKy.objects.filter(diem__isnull=False).count()

    return render(request, "dashboard.html", {
        "tong_sv": tong_sv,
        "tong_dt": tong_dt,
        "tong_dk": tong_dk,
        "da_co_diem": da_co_diem,
    })
