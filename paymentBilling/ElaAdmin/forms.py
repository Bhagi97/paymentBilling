from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
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


class RegisterProfileForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(RegisterProfileForm, self).__init__(*args, **kwargs)
        self.fields['client'].initial = 'null'

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
    email_id = forms.EmailField(
        label='EMAIL ID',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'example@something.com'
            }
        )
    )
    client = forms.CharField(
        label='CLIENT',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Client'
            }
        )
    )
    roles = [
        (1, 'admin'),
        (2, 'supervisor'),
        (3, 'sales')
    ]
    role = forms.TypedChoiceField(
        label='ROLES',
        widget=forms.RadioSelect(
            # attrs={
            #     'class': 'form-control'
            # }
        ),
        choices=roles
    )
    phone_no = forms.CharField(
        label='PHONE NO',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )


