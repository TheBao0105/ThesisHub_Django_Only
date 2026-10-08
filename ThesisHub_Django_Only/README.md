# ThesisHub - Django Only

Đồ án quản lý đồ án tốt nghiệp theo phương án:
- Backend: Django thuần
- Frontend: Django Templates + HTML + CSS
- Không sử dụng JavaScript
- Không sử dụng Django REST Framework
- Database mặc định: SQLite

## 1. Cài đặt

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Mở: http://127.0.0.1:8000/

## 2. Các chức năng

- Dashboard
- Quản lý sinh viên: xem, thêm, sửa, xóa
- Quản lý đề tài: xem, thêm, sửa, xóa
- Quản lý đăng ký: xem, thêm, sửa, xóa
- Cập nhật điểm và xếp loại
- Django Admin
- REST-like JSON endpoints viết trực tiếp bằng Django `JsonResponse`

## 3. API JSON

Sinh viên:
- GET /api/sinhvien/
- GET /api/sinhvien/1/
- POST /api/sinhvien/
- PUT /api/sinhvien/1/
- DELETE /api/sinhvien/1/

Đề tài:
- GET /api/detai/
- GET /api/detai/1/
- POST /api/detai/
- PUT /api/detai/1/
- DELETE /api/detai/1/

Đăng ký:
- GET /api/dangky/
- GET /api/dangky/1/
- POST /api/dangky/
- PUT /api/dangky/1/
- DELETE /api/dangky/1/
- GET /api/dangky/1/diem/

API JSON dùng HTTP + JSON, không cần DRF.

## 4. Ghi chú

Project này không chứa `venv` và không chứa database cũ. Nếu bạn muốn giữ dữ liệu `SV001` hiện có, hãy copy `db.sqlite3` của project cũ vào thư mục này sau khi kiểm tra schema tương thích, hoặc tạo dữ liệu bằng giao diện.
