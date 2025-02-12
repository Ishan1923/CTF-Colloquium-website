from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True)
    rollno = forms.IntegerField(required=True)
    mailid = forms.EmailField(required=True, label="Thapar Mail ID")
    team_name = forms.CharField(max_length=100, required=True)
    hostel = forms.ChoiceField(
        choices=[
            ('A', 'Hostel A'),
            ('B', 'Hostel B'),
            ('C', 'Hostel C'),
            ('D', 'Hostel D'),
            ('E', 'Hostel E'),
            ('F', 'Hostel F'),
            ('G', 'Hostel G'),
            ('H', 'Hostel H'),
            ('I', 'Hostel I'),
            ('J', 'Hostel J'),
            ('K', 'Hostel K'),
            ('L', 'Hostel L'),
            ('M', 'Hostel M'),
            ('N', 'Hostel N'),
            ('O', 'Hostel O'),
            ('PG', 'PG'),
            ('Out-Campus', 'Outside Campus'),
        ],
        required=True,)
    
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "rollno", "mailid", "team_name", "hostel")
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["username"]
        user.email = self.cleaned_data["mailid"]
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            Profile.objects.create(
                user = user,
                rollno = self.cleaned_data['rollno'],
                team_name = self.cleaned_data['team_name'],
                hostel = self.cleaned_data["hostel"],
                mailid = self.cleaned_data['mailid'],
            )
            
        return user


class PasswordResetForm(forms.Form):
    username = forms.CharField();
    secret_key = forms.CharField();
    new_password = forms.CharField(widget=forms.PasswordInput)
    conf_password = forms.CharField(widget = forms.PasswordInput)

    def clean(self):
        cleaned_data =  super().clean()
        username = cleaned_data.get("username")
        secret_key = cleaned_data.get("secret_key")
        new_password = cleaned_data.get("new_password")
        conf_password = cleaned_data.get("conf_password")

        #check if user exists
        if not User.objects.filter(username = username).exists():
            raise forms.ValidationError("user does not exist.")
        
        # Check if secret key is valid (you can change this logic)
        user = User.objects.get(username=username)
        if user.email != secret_key: 
            raise forms.ValidationError("Invalid email-id.")
        
        # Check if passwords match
        if new_password != conf_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data