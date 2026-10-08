from django import forms
from .models import DangKy


class DangKyForm(forms.ModelForm):
    class Meta:
        model = DangKy
        fields = ["sinh_vien", "de_tai", "diem"]
        labels = {
            "sinh_vien": "Sinh viên",
            "de_tai": "Đề tài",
            "diem": "Điểm",
        }
        widgets = {
            "diem": forms.NumberInput(
                attrs={
                    "min": "0",
                    "max": "10",
                    "step": "0.1",
                    "placeholder": "0 - 10",
                }
            ),
        }

    def clean_diem(self):
        diem = self.cleaned_data.get("diem")
        if diem is not None and not 0 <= diem <= 10:
            raise forms.ValidationError("Điểm phải nằm trong khoảng 0 đến 10.")
        return diem

    def clean(self):
        cleaned = super().clean()
        sinh_vien = cleaned.get("sinh_vien")
        de_tai = cleaned.get("de_tai")

        if sinh_vien and de_tai:
            qs = DangKy.objects.filter(
                sinh_vien=sinh_vien,
                de_tai=de_tai
            )
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise forms.ValidationError(
                    "Sinh viên này đã đăng ký đề tài này."
                )
        return cleaned
