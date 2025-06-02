from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  # нужен для установки даты по умолчанию

# Расширенная информация о пользователе (можно дополнять в будущем)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, verbose_name="О себе")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="Аватар")
    website = models.URLField(blank=True, null=True, verbose_name="Сайт / ссылка")
    telegram = models.CharField(max_length=100, blank=True, null=True, verbose_name="Telegram username")
    created_at = models.DateTimeField(default=timezone.now)  # <-- Только default, без auto_now_add

    def __str__(self):
        return f"{self.user.username} профиль"

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
