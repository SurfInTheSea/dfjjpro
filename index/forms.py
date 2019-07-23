from django import forms
from captcha.fields import CaptchaField
 
class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'输入账户'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'输入密码'}))
    captcha = CaptchaField(label='验证码')

class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'输入账户'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'输入密码'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'再次输入密码'}))
    captcha = CaptchaField(label='验证码')
    #captcha_1


class changeInfoBank(forms.Form):
    realName = forms.CharField( max_length=128, widget=forms.Textarea(attrs={'class': 'n-dd'}) )
    bank = forms.CharField(max_length=128, widget=forms.Textarea(attrs={'class': 'n-dd'}) )
    bank_details = forms.CharField(max_length=256, widget=forms.Textarea(attrs={'class': 'n-dd'}) )
    bank_acount = forms.CharField(max_length=256, widget=forms.Textarea(attrs={'class': 'n-dd'}) )
    pay_name = forms.CharField(max_length=128, widget=forms.Textarea(attrs={'class': 'n-dd'}) )

'''


content  = forms.CharField(widget=forms.Textarea)



	<span class="n-dt">真实姓名</span><span class="n-dd">{{ request.session.realName }}</span>

 	realName = models.CharField('真实姓名', max_length=128, default='')
    bank = models.CharField('银行', max_length=128, default='')
    bank_details = models.CharField('开户行', max_length=256, default='')
    bank_acount = models.CharField('卡号', max_length=256, default='')
    pay_name = models.CharField('利息账户', max_length=128, default='')
'''








