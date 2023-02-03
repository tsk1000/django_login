from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

from .forms import LoginAuthenticationForm


class Login(LoginView):
    """ ログインビュー """

    template_name = "login/login.html"
    authentication_form = LoginAuthenticationForm # 認証用フォーム

    def form_valid(self, form):
        # ログイン処理実施
        auth_login(self.request, form.get_user())
        # ユーザーでログイン後の画面を変更する
        return redirect("/sample/")
