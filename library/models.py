from django.db import models
from django.utils import timezone

# Модель книги / ресурса
class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    author = models.CharField(max_length=255, blank=True, null=True, verbose_name="Автор")
    description = models.TextField(verbose_name="Описание")
    link = models.URLField(blank=True, null=True, verbose_name="Ссылка на источник")
    cover_image = models.ImageField(upload_to='books/', blank=True, null=True, verbose_name="Обложка")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата добавления")
    is_recommended = models.BooleanField(default=False, verbose_name="Рекомендую")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга / Ресурс"
        verbose_name_plural = "Библиотека"
        ordering = ['-created_at']
