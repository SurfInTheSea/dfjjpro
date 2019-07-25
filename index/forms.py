from django import forms
from captcha.fields import CaptchaField
 
class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={
                                                                                    'class': 'form-control',
                                                                                    'placeholder': '输入账户'
                                                                                }))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={
                                                                                    'class': 'form-control',
                                                                                    'placeholder': '输入密码'
                                                                                }))
    captcha = CaptchaField(label='验证码')

class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={
                                                                                    'class': 'form-control',
                                                                                    'placeholder': '输入账户'
                                                                                }))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={
                                                                                    'class': 'form-control',
                                                                                    'placeholder': '输入密码'
                                                                                }))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={
                                                                                    'class': 'form-control',
                                                                                    'placeholder': '再次输入密码'
                                                                                }))
    captcha = CaptchaField(label='验证码')
    # captcha_1


class changeInfoBank(forms.Form):
    realName = forms.CharField(max_length=128, widget=forms.Textarea(attrs={'class': 'n-dd'}))
    bank = forms.CharField(max_length=128, widget=forms.Textarea(attrs={'class': 'n-dd'}))
    bank_details = forms.CharField(max_length=256, widget=forms.Textarea(attrs={'class': 'n-dd'}))
    bank_acount = forms.CharField(max_length=256, widget=forms.Textarea(attrs={'class': 'n-dd'}))
    pay_name = forms.CharField(max_length=128, widget=forms.Textarea(attrs={'class': 'n-dd'}))









