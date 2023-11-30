from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Address

class CustomUserCreationForm(UserCreationForm):
    street = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)
    county = forms.CharField(max_length=255)
    post_code = forms.CharField(max_length=255)

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('username', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()

        # Create associated Address instance
        Address.objects.create(
            customer=user,
            street=self.cleaned_data['street'],
            city=self.cleaned_data['city'],
            county=self.cleaned_data['county'],
            post_code=self.cleaned_data['post_code']
        )

        return user
    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email',)
