from django.db import models


class DeTai(models.Model):
    ma_detai = models.CharField(max_length=20, unique=True)
    ten_detai = models.CharField(max_length=200)
    mo_ta = models.TextField(blank=True)
    trang_thai = models.CharField(max_length=50, default="Chưa đăng ký")

    class Meta:
        ordering = ["ma_detai"]
        verbose_name = "Đề tài"
        verbose_name_plural = "Đề tài"

    def __str__(self):
        return f"{self.ma_detai} - {self.ten_detai}"
