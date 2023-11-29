from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Address

class AddressInline(admin.TabularInline):
    model = Address
    extra = 2 

class CustomUserAdmin(UserAdmin):
    #add_form = CustomUserCreationForm
    #form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username']

    inlines = [AddressInline]

admin.site.register(CustomUser, CustomUserAdmin)

