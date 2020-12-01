from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser 
        fields = UserCreationForm.Meta.fields + ('age', 'phone_number', 'salary_amount',)

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = UserChangeForm.Meta.fields # допишу что понадобится