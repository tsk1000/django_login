from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate


class LoginAuthenticationForm(forms.Form):
    """ ログイン認証フォーム
    """
    # ログインID
    login_id = forms.CharField(
        required = True,
        label="ログインID",
        widget=forms.TextInput(
            attrs={'id': 'loginID', 'class': 'loginidtext'
                , 'placeholder' :'ログインID', 'autofocus': True
                , 'onkeydown': 'if(event.keyCode==13){loginButtonClick();return false};'}
        ),
    )
    # パスワード
    password = forms.CharField(
        required = True,
        label="パスワード",
        strip=False,
        widget=forms.PasswordInput(
            attrs={'id': 'password', 'class': 'passtext'
                , 'placeholder' :'パスワード', 'autocomplete': 'current-password'
                , 'onkeydown': 'if(event.keyCode==13){loginButtonClick();return false};'}
        ),
    )
    login_error_msg = " * ログインID、またはパスワードが正しくありません。"

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.user_cache = None

    def clean(self):
        # ログインID(メールアドレス)
        email = self.cleaned_data.get('login_id')
        # パスワード
        password = self.cleaned_data.get('password')

        # 該当するユーザーを取得する
        self.user_cache = authenticate(email=email, password=password)

        # 存在しない場合(None)はログイン失敗
        if self.user_cache is None:
            messages.error(self.request, self.login_error_msg)
            raise forms.ValidationError(self.login_error_msg)

        return self.cleaned_data

    def get_user(self):
        return self.user_cache
    