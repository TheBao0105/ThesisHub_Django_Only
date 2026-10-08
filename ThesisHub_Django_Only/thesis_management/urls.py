from django.contrib import admin
from django.urls import path

from sinhvien.views import (
    sinhvien_list,
    sinhvien_create,
    sinhvien_edit,
    sinhvien_delete,
    sinhvien_api,
)
from detai.views import (
    detai_list,
    detai_create,
    detai_edit,
    detai_delete,
    detai_api,
)
from dangky.views import (
    dangky_list,
    dangky_create,
    dangky_edit,
    dangky_delete,
    dangky_diem,
    dangky_api,
    dangky_diem_api,
)
from .views import dashboard


urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("admin/", admin.site.urls),

    path("sinhvien/", sinhvien_list, name="sinhvien_list"),
    path("sinhvien/them/", sinhvien_create, name="sinhvien_create"),
    path("sinhvien/<int:id>/sua/", sinhvien_edit, name="sinhvien_edit"),
    path("sinhvien/<int:id>/xoa/", sinhvien_delete, name="sinhvien_delete"),

    path("detai/", detai_list, name="detai_list"),
    path("detai/them/", detai_create, name="detai_create"),
    path("detai/<int:id>/sua/", detai_edit, name="detai_edit"),
    path("detai/<int:id>/xoa/", detai_delete, name="detai_delete"),

    path("dangky/", dangky_list, name="dangky_list"),
    path("dangky/them/", dangky_create, name="dangky_create"),
    path("dangky/<int:id>/sua/", dangky_edit, name="dangky_edit"),
    path("dangky/<int:id>/xoa/", dangky_delete, name="dangky_delete"),
    path("dangky/<int:id>/diem/", dangky_diem, name="dangky_diem"),

    # JSON API - Django thuần
    path("api/sinhvien/", sinhvien_api, name="sinhvien_api"),
    path("api/sinhvien/<int:id>/", sinhvien_api, name="sinhvien_api_detail"),

    path("api/detai/", detai_api, name="detai_api"),
    path("api/detai/<int:id>/", detai_api, name="detai_api_detail"),

    path("api/dangky/", dangky_api, name="dangky_api"),
    path("api/dangky/<int:id>/", dangky_api, name="dangky_api_detail"),
    path("api/dangky/<int:id>/diem/", dangky_diem_api, name="dangky_diem_api"),
]
