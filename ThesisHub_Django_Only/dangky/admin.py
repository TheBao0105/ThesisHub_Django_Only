from django.contrib import admin
from .models import DangKy

@admin.register(DangKy)
class DangKyAdmin(admin.ModelAdmin):
    list_display = (
        "id", "sinh_vien", "de_tai",
        "ngay_dang_ky", "diem", "xep_loai"
    )
    list_filter = ("diem",)
