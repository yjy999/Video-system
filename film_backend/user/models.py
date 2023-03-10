from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class myuser(AbstractUser):
    #uid = models.CharField(max_length=8,null=True)
    #name = models.CharField(max_length=30,null=True,blank=True,verbose_name="姓名")
    gender_choice=(('1','用户'),('2','管理员'))
    roles = models.CharField(max_length=10,choices=gender_choice,default="1",verbose_name="角色")


    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.username