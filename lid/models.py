from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class UsrSendAnswer(models.Model):
    usr = models.ForeignKey(User, related_name='send_answ', on_delete=models.CASCADE, )
    answr = models.BooleanField(verbose_name='Согласен на подписку?', default='False')
    def __str__(self):
        return self.usr
    class Meta:
        verbose_name='Справочник (Согласен на подписку?)'
        verbose_name_plural='Справочник (Согласен на подписку?)'


