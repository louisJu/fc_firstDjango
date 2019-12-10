from django.db import models

# Create your models here.

class Fcuser(models.Model):
    username = models.CharField(max_length=32,
                                verbose_name='사용자명')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    reg_dttm = models.DateTimeField(auto_now_add=True,
                                    verbose_name='등록시간')
    user_email = models.EmailField(max_length=128,
                                   verbose_name='e-mail')

    def __str__(self):
        return self.username
    class Meta:
        db_table = 'fcuser01'
        verbose_name_plural='사용자'
