from django.db import models

# Create your models here.
class Task (models.Model):
    title = models.CharField(max_length=155, verbose_name = "Заголовка")
    description = models.TextField(verbose_name = "Описание")
    completed = models.BooleanField(default=False, verbose_name = "статус выполнения")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "время создания задачи")
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name=""
        verbose_name_plural="Основные задания "
