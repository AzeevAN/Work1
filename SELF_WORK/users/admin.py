from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import MyUserChangeForm, MyUserCreationForm
from .models import CustomUser

class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = CustomUser 
    list_display = ["username", "email", "salary_amount", 'age', 'phone_number']

admin.site.register(CustomUser, MyUserAdmin) 