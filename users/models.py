from django.db import models


class User(models.Model):
    class Meta:
        db_table = 'users'
        verbose_name = '사용자'
        verbose_name_plural = verbose_name

    name = models.CharField(
        verbose_name='이름',
        max_length=16
    )

