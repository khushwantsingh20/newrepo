from django import forms
from accounts.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        # Adding placeholders to form fields
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'









from django import forms
from django.contrib.auth.forms import UserCreationForm

# forms.py
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['img','name', 'phone', 'address', 'state', 'postcode', 'landmark']

# forms.py

# forms.py
from django import forms
from .models import Profile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'landmark', 'state', 'postcode']



# myapp/forms.py


from django.contrib.auth.forms import PasswordChangeForm

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(user, *args, **kwargs)

        self.fields['new_password1'].help_text = None  # Removes all help text
        # self.fields['new_password1'].widget.attrs.pop("autocomplete", None)  # Removes autocomplete attribute

        # Customize the labels or add any extra fields if needed
        self.fields['old_password'].label = 'Old Password'
        self.fields['new_password1'].label = 'New Password'
        self.fields['new_password2'].label = 'Confirm  Password'
