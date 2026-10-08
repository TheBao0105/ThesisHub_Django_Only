from django import forms
from .models import DeTai


class DeTaiForm(forms.ModelForm):
    class Meta:
        model = DeTai
        fields = ["ma_detai", "ten_detai", "mo_ta", "trang_thai"]
        labels = {
            "ma_detai": "Mã đề tài",
            "ten_detai": "Tên đề tài",
            "mo_ta": "Mô tả",
            "trang_thai": "Trạng thái",
        }
        widgets = {
            "ma_detai": forms.TextInput(attrs={"placeholder": "VD: DT001"}),
            "ten_detai": forms.TextInput(attrs={"placeholder": "Tên đề tài"}),
            "mo_ta": forms.Textarea(attrs={"rows": 5, "placeholder": "Mô tả đề tài"}),
            "trang_thai": forms.TextInput(attrs={"placeholder": "Chưa đăng ký"}),
        }
