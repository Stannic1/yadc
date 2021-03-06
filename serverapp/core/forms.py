# Signup form class

from django.contrib.auth.forms import UserCreationForm
from .models import User
 
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'age', 'school')

class SignInForm():
    class Meta:
        model = User
        fields = ('email', 'password')
