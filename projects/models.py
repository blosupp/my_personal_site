from django.db import models
from django.utils import timezone

# Проект в портфолио
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название проекта")
    description = models.TextField(verbose_name="Описание проекта")
    link = models.URLField(blank=True, null=True, verbose_name="Ссылка на проект")
    image = models.ImageField(upload_to='projects/', blank=True, null=True, verbose_name="Изображение проекта")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата добавления")
    is_featured = models.BooleanField(default=False, verbose_name="Выводить на главной")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"