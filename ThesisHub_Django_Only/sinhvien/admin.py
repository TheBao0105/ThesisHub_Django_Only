from django.contrib import admin
from .models import SinhVien

@admin.register(SinhVien)
class SinhVienAdmin(admin.ModelAdmin):
    list_display = ("id", "ma_sinhvien", "ho_ten", "email", "lop")
    search_fields = ("ma_sinhvien", "ho_ten", "email")
