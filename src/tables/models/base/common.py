from django.db import models


class Common(models.Model):
    """ 共通 モデル """

    # 作成者ID
    create_id = models.CharField(null=True, max_length=50)
    # 作成日時
    create_at = models.DateTimeField(null=True, auto_now_add=True)
    # 更新者ID
    update_id = models.CharField(null=True, max_length=50)
    # 更新日時
    update_at = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        # migrate でテーブルを作成しないように True に設定
        abstract = True
