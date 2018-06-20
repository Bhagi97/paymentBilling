from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label='USERNAME',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }
        )
    )
    password = forms.CharField(
        label='PASSWORD',
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )
    )