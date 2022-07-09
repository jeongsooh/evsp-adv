from django.db import models
from evuser.models import Evuser
from evcharger.models import Evcharger

# Create your models here.

class Msglog(models.Model):
  cpname = models.CharField(max_length=128, verbose_name='충전기번호')
  username = models.CharField(max_length=128, verbose_name='사용자명')
  msg_direction = models.IntegerField(verbose_name='메세지오리진')
  msg_name = models.CharField(max_length=128, verbose_name='메세지이름')
  msg_content = models.TextField(verbose_name='메세지본문')
  connection_id = models.IntegerField(verbose_name='커넥션아이디')
  register_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록일시')

  # def __str__(self):
  #   return self.msg_name

  class Meta:
    db_table = 'evsp_msglog'
    verbose_name = '메세지로그정보'
    verbose_name_plural = '메세지로그정보'
