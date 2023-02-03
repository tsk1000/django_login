from django.db import models


class Delete(models.TextChoices):
    """ 削除済区分\n
        未削除:0, 削除済:1
    """
    NOT = '0' , '未削除'
    DELETED = '1', '削除済'

SAKUJO_CHOICES = Delete.choices
