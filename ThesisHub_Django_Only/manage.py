#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thesis_management.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Không thể import Django. Hãy kích hoạt venv và chạy: pip install django"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
