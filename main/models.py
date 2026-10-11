from django.db import models


class Announcement(models.Model):
    title = models.CharField("Заголовок", max_length=150)
    text = models.TextField("Текст")
    is_active = models.BooleanField("Показывать на сайте", default=True)
    created_at = models.DateTimeField("Создано", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.title


class Registration(models.Model):
    last_name = models.CharField("Фамилия", max_length=60)
    first_name = models.CharField("Имя", max_length=60)
    phone = models.CharField("Номер телефона", max_length=25)
    school_class = models.CharField("Класс", max_length=10)
    created_at = models.DateTimeField("Дата записи", auto_now_add=True)

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.school_class})"
