import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from .forms import DangKyForm
from .models import DangKy


def dangky_list(request):
    dangkys = DangKy.objects.select_related("sinh_vien", "de_tai").all()
    return render(request, "dangky/list.html", {
        "dangkys": dangkys
    })


def dangky_create(request):
    if request.method == "POST":
        form = DangKyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dangky_list")
    else:
        form = DangKyForm()

    return render(request, "dangky/form.html", {
        "form": form,
        "title": "Thêm đăng ký",
        "button_text": "Thêm đăng ký",
    })


def dangky_edit(request, id):
    dangky = get_object_or_404(DangKy, id=id)

    if request.method == "POST":
        form = DangKyForm(request.POST, instance=dangky)
        if form.is_valid():
            form.save()
            return redirect("dangky_list")
    else:
        form = DangKyForm(instance=dangky)

    return render(request, "dangky/form.html", {
        "form": form,
        "title": "Sửa đăng ký / cập nhật điểm",
        "button_text": "Lưu thay đổi",
    })


def dangky_delete(request, id):
    dangky = get_object_or_404(DangKy, id=id)
    if request.method == "POST":
        dangky.delete()
        return redirect("dangky_list")

    return render(request, "confirm_delete.html", {
        "object": dangky,
        "back_url": "dangky_list",
        "title": "Xóa đăng ký",
    })


def dangky_diem(request, id):
    dangky = get_object_or_404(
        DangKy.objects.select_related("sinh_vien", "de_tai"),
        id=id
    )
    return render(request, "dangky/diem.html", {
        "dangky": dangky
    })


@require_http_methods(["GET", "POST", "PUT", "DELETE"])
def dangky_api(request, id=None):
    if request.method == "GET":
        qs = DangKy.objects.select_related("sinh_vien", "de_tai")

        if id is None:
            data = [
                {
                    "id": item.id,
                    "sinh_vien": item.sinh_vien.id,
                    "ma_sinhvien": item.sinh_vien.ma_sinhvien,
                    "ho_ten": item.sinh_vien.ho_ten,
                    "de_tai": item.de_tai.id,
                    "ma_detai": item.de_tai.ma_detai,
                    "ten_detai": item.de_tai.ten_detai,
                    "ngay_dang_ky": item.ngay_dang_ky,
                    "diem": item.diem,
                    "xep_loai": item.xep_loai,
                }
                for item in qs
            ]
            return JsonResponse(data, safe=False)

        item = get_object_or_404(qs, id=id)
        return JsonResponse({
            "id": item.id,
            "sinh_vien": item.sinh_vien.id,
            "ma_sinhvien": item.sinh_vien.ma_sinhvien,
            "ho_ten": item.sinh_vien.ho_ten,
            "de_tai": item.de_tai.id,
            "ma_detai": item.de_tai.ma_detai,
            "ten_detai": item.de_tai.ten_detai,
            "ngay_dang_ky": item.ngay_dang_ky,
            "diem": item.diem,
            "xep_loai": item.xep_loai,
        })

    try:
        data = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON không hợp lệ."}, status=400)

    if request.method == "POST":
        form = DangKyForm(data)
        if not form.is_valid():
            return JsonResponse({"errors": form.errors.get_json_data()}, status=400)
        item = form.save()
        return JsonResponse({
            "id": item.id,
            "message": "Đăng ký thành công.",
        }, status=201)

    item = get_object_or_404(DangKy, id=id)

    if request.method == "PUT":
        form = DangKyForm(data, instance=item)
        if not form.is_valid():
            return JsonResponse({"errors": form.errors.get_json_data()}, status=400)
        item = form.save()
        return JsonResponse({
            "id": item.id,
            "message": "Cập nhật đăng ký thành công.",
            "diem": item.diem,
            "xep_loai": item.xep_loai,
        })

    item.delete()
    return JsonResponse({"message": "Xóa đăng ký thành công."})


def dangky_diem_api(request, id):
    if request.method != "GET":
        return JsonResponse({"error": "Chỉ hỗ trợ GET."}, status=405)

    item = get_object_or_404(
        DangKy.objects.select_related("sinh_vien", "de_tai"),
        id=id
    )

    return JsonResponse({
        "ma_sinhvien": item.sinh_vien.ma_sinhvien,
        "ho_ten": item.sinh_vien.ho_ten,
        "ma_detai": item.de_tai.ma_detai,
        "ten_detai": item.de_tai.ten_detai,
        "diem": item.diem,
        "xep_loai": item.xep_loai,
    })
