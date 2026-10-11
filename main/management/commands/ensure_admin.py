import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Создаёт админа из переменных ADMIN_USERNAME / ADMIN_PASSWORD, если его ещё нет"

    def handle(self, *args, **options):
        username = os.environ.get("ADMIN_USERNAME")
        password = os.environ.get("ADMIN_PASSWORD")
        if not username or not password:
            self.stdout.write("ADMIN_USERNAME/ADMIN_PASSWORD не заданы — пропускаю")
            return
        User = get_user_model()
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, password=password)
            self.stdout.write(f"Админ {username} создан")
