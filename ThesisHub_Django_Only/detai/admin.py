from django.contrib import admin
from .models import DeTai

@admin.register(DeTai)
class DeTaiAdmin(admin.ModelAdmin):
    list_display = ("id", "ma_detai", "ten_detai", "trang_thai")
    search_fields = ("ma_detai", "ten_detai")
