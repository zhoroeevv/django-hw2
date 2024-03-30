from django.db import models

class InfoUser(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = "Имя пользователя"
    )

    image = models.ImageField(
        upload_to="info_user/",
        verbose_name="Фотография пользователя"
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Данные пользователя"
        verbose_name_plural = "Данные пользователей"
        