from django import forms

class Register(forms.Form):
    username = forms.CharField(required=True,label="用户名",error_messages={"required":"这个东西咋能为空呢？"},disabled=True)
    password = forms.CharField(max_length=32,widget=forms.PasswordInput,label="密码",initial="hello world",help_text="请输入6位密码")
    email = forms.EmailField()