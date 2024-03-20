from django.contrib import admin
from .models import Form

class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name","email","occupation")
    search_fields = ("first_name","email","occupation")
    list_filter = ("occupation","first_name")

admin.site.register(Form,FormAdmin)

