from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


User = get_user_model()

class ContactMessage(models.Model):
    name    = models.CharField("Имя", max_length=80)
    email   = models.EmailField("E‑mail")
    message = models.TextField("Сообщение")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

class PageHit(models.Model):
    path = models.CharField(max_length=255)
    ip = models.GenericIPAddressField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    referer = models.CharField(max_length=512, blank=True)  # уже добавлено
    user_agent = models.CharField(max_length=512, blank=True)  # ← добавь ЭТО
    created = models.DateTimeField(auto_now_add=True)

class PageCounter(models.Model):
    """Общее количество просмотров по URL"""
    path  = models.CharField(max_length=255, unique=True)
    hits  = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.path}: {self.hits}"


class Skill(models.Model):
    title       = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon        = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title