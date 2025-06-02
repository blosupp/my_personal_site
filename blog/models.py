from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone

# Модель статьи в блоге
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(unique=True, blank=True, verbose_name="URL")  # slug будет формироваться автоматически
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name="Автор")
    content = models.TextField(verbose_name="Содержание")
    image = models.ImageField(upload_to='blog/', blank=True, null=True, verbose_name="Обложка")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    published = models.BooleanField(default=False, verbose_name="Опубликовано")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # если slug не задан — генерируем его из заголовка
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-created_at']  # сначала новые
