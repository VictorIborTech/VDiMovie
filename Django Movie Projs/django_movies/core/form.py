from django.forms import ModelForm
from .models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['uuid'] # I exclude it so it will be generated automatically from the Backend

        
