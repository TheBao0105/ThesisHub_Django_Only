from django.db import models
from sinhvien.models import SinhVien
from detai.models import DeTai


class DangKy(models.Model):
    sinh_vien = models.ForeignKey(
        SinhVien,
        on_delete=models.CASCADE,
        related_name="dang_kys"
    )
    de_tai = models.ForeignKey(
        DeTai,
        on_delete=models.CASCADE,
        related_name="dang_kys"
    )
    ngay_dang_ky = models.DateField(auto_now_add=True)
    diem = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ["-ngay_dang_ky", "-id"]
        verbose_name = "Đăng ký"
        verbose_name_plural = "Đăng ký"

    def __str__(self):
        return f"{self.sinh_vien.ma_sinhvien} - {self.de_tai.ma_detai}"

    @property
    def xep_loai(self):
        if self.diem is None:
            return "Chưa có điểm"
        if self.diem >= 8.5:
            return "Giỏi"
        if self.diem >= 7:
            return "Khá"
        if self.diem >= 5:
            return "Trung bình"
        return "Không đạt"
