from django.contrib import admin
from .models import Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("username", "rollno", "team_name", "hostel", "mailid")
admin.site.register(Profile, ProfileAdmin)