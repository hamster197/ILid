from django.contrib import admin

# Register your models here.

from lid.models import UsrSendAnswer

class UsrSendAnswrFields(admin.ModelAdmin):
    list_display = ('pk','usr','answr')


admin.site.register(UsrSendAnswer, UsrSendAnswrFields)
