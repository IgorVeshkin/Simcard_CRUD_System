from django import forms


class CRUDSystemLoginForm(forms.Form):
    Username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Имя пользователя", "name": "username"}), max_length=255)
    Password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Пароль", "name": "password"}), max_length=100)