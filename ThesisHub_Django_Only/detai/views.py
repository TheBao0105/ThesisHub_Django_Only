import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from .forms import DeTaiForm
from .models import DeTai


def detai_list(request):
    return render(request, "detai/list.html", {
        "detais": DeTai.objects.all()
    })


def detai_create(request):
    if request.method == "POST":
        form = DeTaiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("detai_list")
    else:
        form = DeTaiForm()

    return render(request, "detai/form.html", {
        "form": form,
        "title": "Thêm đề tài",
        "button_text": "Thêm đề tài",
    })


def detai_edit(request, id):
    detai = get_object_or_404(DeTai, id=id)

    if request.method == "POST":
        form = DeTaiForm(request.POST, instance=detai)
        if form.is_valid():
            form.save()
            return redirect("detai_list")
    else:
        form = DeTaiForm(instance=detai)

    return render(request, "detai/form.html", {
        "form": form,
        "title": "Sửa đề tài",
        "button_text": "Lưu thay đổi",
    })


def detai_delete(request, id):
    detai = get_object_or_404(DeTai, id=id)
    if request.method == "POST":
        detai.delete()
        return redirect("detai_list")

    return render(request, "confirm_delete.html", {
        "object": detai,
        "back_url": "detai_list",
        "title": "Xóa đề tài",
    })


@require_http_methods(["GET", "POST", "PUT", "DELETE"])
def detai_api(request, id=None):
    if request.method == "GET":
        if id is None:
            data = list(DeTai.objects.values(
                "id", "ma_detai", "ten_detai", "mo_ta", "trang_thai"
            ))
            return JsonResponse(data, safe=False)

        detai = get_object_or_404(DeTai, id=id)
        return JsonResponse({
            "id": detai.id,
            "ma_detai": detai.ma_detai,
            "ten_detai": detai.ten_detai,
            "mo_ta": detai.mo_ta,
            "trang_thai": detai.trang_thai,
        })

    try:
        data = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON không hợp lệ."}, status=400)

    if request.method == "POST":
        form = DeTaiForm(data)
        if not form.is_valid():
            return JsonResponse({"errors": form.errors.get_json_data()}, status=400)
        detai = form.save()
        return JsonResponse({
            "id": detai.id,
            "ma_detai": detai.ma_detai,
            "ten_detai": detai.ten_detai,
            "mo_ta": detai.mo_ta,
            "trang_thai": detai.trang_thai,
        }, status=201)

    detai = get_object_or_404(DeTai, id=id)

    if request.method == "PUT":
        form = DeTaiForm(data, instance=detai)
        if not form.is_valid():
            return JsonResponse({"errors": form.errors.get_json_data()}, status=400)
        detai = form.save()
        return JsonResponse({
            "id": detai.id,
            "ma_detai": detai.ma_detai,
            "ten_detai": detai.ten_detai,
            "mo_ta": detai.mo_ta,
            "trang_thai": detai.trang_thai,
        })

    detai.delete()
    return JsonResponse({"message": "Xóa đề tài thành công."})
