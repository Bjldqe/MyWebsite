from django import forms
from django.contrib.auth.models import User

from .models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=32,widget=forms.TextInput(attrs={
        'class':'input','placeholder':'请输入用户名/邮箱'
    }))
    password = forms.CharField(label='密码', min_length=6, widget=forms.PasswordInput(attrs={
        'class':'input','placeholder':'请输入密码'
    }))

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username == password:
            raise forms.ValidationError('密码不可与用户名相同')
        return password
    
class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label='邮箱', min_length=3, widget=forms.EmailInput(attrs={
        'class': 'input', 'placeholder': '请输入邮箱'}))
    password = forms.CharField(label='密码', min_length=6, widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': '请输入密码密码'}))
    password1 = forms.CharField(label='请再次输入密码', min_length=6, widget=forms.PasswordInput(attrs={
        'class': 'input', 'placeholder': '两次密码请保持一致'}))

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError('该邮箱已被注册!')
        return email

    def clean_password1(self):
        data = self.cleaned_data
        password = data['password']
        password1 = data['password1']
        if password != password1:
            raise forms.ValidationError('两次输入的密码不一致,请重新输入!')
        return password
class ForgetPwdForm(forms.Form):
    """ 填写邮箱地址表单 """
    email = forms.EmailField(label='请输入你的邮箱', min_length=4, widget=forms.EmailInput(attrs={
        'class': 'input', 'placeholder': '用户名/邮箱'
    }))

class ModifyPwdForm(forms.Form):
	"""Form definition for UserProfile."""
	password = forms.CharField(label='输入新密码', min_length=6, 
		widget=forms.PasswordInput(attrs={'class':'input', 'placeholder':'输入新密码'}))

class UserForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'input', 'disabled':'disabled'
    }))

    class Meta:
        model = User
        fields = ('email',)


class UserProfileForm(forms.ModelForm):
    """Form definition for UserInfo."""
 
    class Meta:
        """Meta definition for UserInfoform."""

        model = UserProfile
        fields = ('nick_name','desc', 'signature', 'birthday',  'gender', 'address', 'image')
