import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

from tables.models.base.common import Common


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """ 指定された電子メールとパスワードでユーザーを作成して保存します。 """

        if not email:
            raise ValueError('email is required.')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, Common):
    """ ユーザマスタ """

    # ID
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    # メールアドレス
    email = models.CharField(max_length=256, unique=True)
    # 姓
    last_name = models.CharField(max_length=50)
    # 名
    first_name = models.CharField(max_length=50)
    # セイ
    last_name_kana = models.CharField(max_length=50)
    # メイ
    first_name_kana = models.CharField(max_length=50)
    # パスワード
    password = models.CharField(max_length=128)
    # アクティブ状態
    is_active = models.BooleanField(default=True)

    # Userクラスの中にあるobjectsという変数は、views.pyなどでUserモデルの情報を参照するときに使います。
    objects = UserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'user'

    def get_full_name(self):
        """ スペースを挟んでフルネーム(漢字)を取得する """
        return f'{self.last_name} {self.first_name}'

    def get_full_name_kana(self):
        """ スペースを挟んでフルネーム(カナ)を取得する """
        return f'{self.last_name_kana} {self.first_name_kana}'
