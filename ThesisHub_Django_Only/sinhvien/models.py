from django.db import models


class SinhVien(models.Model):
    ma_sinhvien = models.CharField(max_length=20, unique=True)
    ho_ten = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    lop = models.CharField(max_length=50)

    class Meta:
        ordering = ["ma_sinhvien"]
        verbose_name = "Sinh viên"
        verbose_name_plural = "Sinh viên"

    def __str__(self):
        return f"{self.ma_sinhvien} - {self.ho_ten}"
