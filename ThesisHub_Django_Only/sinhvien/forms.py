from django import forms
from .models import SinhVien


class SinhVienForm(forms.ModelForm):
    class Meta:
        model = SinhVien
        fields = ["ma_sinhvien", "ho_ten", "email", "lop"]
        labels = {
            "ma_sinhvien": "Mã sinh viên",
            "ho_ten": "Họ tên",
            "email": "Email",
            "lop": "Lớp",
        }
        widgets = {
            "ma_sinhvien": forms.TextInput(attrs={"placeholder": "VD: SV001"}),
            "ho_ten": forms.TextInput(attrs={"placeholder": "Nguyễn Văn A"}),
            "email": forms.EmailInput(attrs={"placeholder": "a@gmail.com"}),
            "lop": forms.TextInput(attrs={"placeholder": "K44A"}),
        }
