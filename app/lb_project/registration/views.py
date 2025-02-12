from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .forms import PasswordResetForm

def  register(request):
    # return render(request, 'website/register.html')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print("#############################",form.is_valid())
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful.")
            print("REGISTRATION SUCCESSFUL!")
            return redirect('done/')
        else:
            print("FORM ERRORS: ", form.errors)
            messages.error(request, 'Please fix the erros below.')
    else:
        form = CustomUserCreationForm()
    

    return render(request, 'website\\register.html', {'form' : form})

def done(request):
    return render(request, "website\confirmation.html")


def password_reset_view(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        print("#############################",form.is_valid())
        print("FROM ERRORS: ", form.errors)
        if form.is_valid():
            print("##################################Setting New Password")
            username = form.cleaned_data["username"]
            new_password = form.cleaned_data["new_password"]
            user = User.objects.get(username=username)
            user.password = make_password(new_password)
            user.save()
            print("REDIRECTING")
            return redirect("done/")
    else:
        form = PasswordResetForm()
    return render(request, "passwordReset/password_reset_form.html", {"form": form})

def password_reset_done(request):
    return render(request, "passwordReset/password_reset_complete.html")
