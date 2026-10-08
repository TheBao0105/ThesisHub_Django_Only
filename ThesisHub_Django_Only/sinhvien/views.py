import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from .forms import SinhVienForm
from .models import SinhVien


def sinhvien_list(request):
    return render(request, "sinhvien/list.html", {
        "sinhviens": SinhVien.objects.all()
    })


def sinhvien_create(request):
    if request.method == "POST":
        form = SinhVienForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("sinhvien_list")
    else:
        form = SinhVienForm()

    return render(request, "sinhvien/form.html", {
        "form": form,
        "title": "Thêm sinh viên",
        "button_text": "Thêm sinh viên",
    })


def sinhvien_edit(request, id):
    sinhvien = get_object_or_404(SinhVien, id=id)

    if request.method == "POST":
        form = SinhVienForm(request.POST, instance=sinhvien)
        if form.is_valid():
            form.save()
            return redirect("sinhvien_list")
    else:
        form = SinhVienForm(instance=sinhvien)

    return render(request, "sinhvien/form.html", {
        "form": form,
        "title": "Sửa sinh viên",
        "button_text": "Lưu thay đổi",
    })


def sinhvien_delete(request, id):
    sinhvien = get_object_or_404(SinhVien, id=id)
    if request.method == "POST":
        sinhvien.delete()
        return redirect("sinhvien_list")

    return render(request, "confirm_delete.html", {
        "object": sinhvien,
        "back_url": "sinhvien_list",
        "title": "Xóa sinh viên",
    })


@require_http_methods(["GET", "POST", "PUT", "DELETE"])
def sinhvien_api(request, id=None):
    if request.method == "GET":
        if id is None:
            data = list(SinhVien.objects.values(
                "id", "ma_sinhvien", "ho_ten", "email", "lop"
            ))
            return JsonResponse(data, safe=False)

        sinhvien = get_object_or_404(SinhVien, id=id)
        return JsonResponse({
            "id": sinhvien.id,
            "ma_sinhvien": sinhvien.ma_sinhvien,
            "ho_ten": sinhvien.ho_ten,
            "email": sinhvien.email,
            "lop": sinhvien.lop,
        })

    try:
        data = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON không hợp lệ."}, status=400)

    if request.method == "POST":
        form = SinhVienForm(data)
        if not form.is_valid():
            return JsonResponse({"errors": form.errors.get_json_data()}, status=400)
        sinhvien = form.save()
        return JsonResponse({
            "id": sinhvien.id,
            "ma_sinhvien": sinhvien.ma_sinhvien,
            "ho_ten": sinhvien.ho_ten,
            "email": sinhvien.email,
            "lop": sinhvien.lop,
        }, status=201)

    sinhvien = get_object_or_404(SinhVien, id=id)

    if request.method == "PUT":
        form = SinhVienForm(data, instance=sinhvien)
        if not form.is_valid():
            return JsonResponse({"errors": form.errors.get_json_data()}, status=400)
        sinhvien = form.save()
        return JsonResponse({
            "id": sinhvien.id,
            "ma_sinhvien": sinhvien.ma_sinhvien,
            "ho_ten": sinhvien.ho_ten,
            "email": sinhvien.email,
            "lop": sinhvien.lop,
        })

    sinhvien.delete()
    return JsonResponse({"message": "Xóa sinh viên thành công."})
