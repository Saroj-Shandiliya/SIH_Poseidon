# console/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class ConsoleAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['zoneID', 'secretKey']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')  # Using 'username' for zoneID
        password = cleaned_data.get('password')  # Using 'password' for secretKey

        # Check if a user with the given credentials exists
        user = CustomUser.objects.filter(zoneID=username, secretKey=password).first()
        if not user:
            raise forms.ValidationError('Invalid username or password.')

        return cleaned_data

# console/forms.py
from django import forms
from .models import CustomUser

class CustomUserAdminForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'zoneID', 'secretKey']
