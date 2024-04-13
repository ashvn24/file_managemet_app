from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(Groups)
admin.site.register(Folder)
admin.site.register(File)
