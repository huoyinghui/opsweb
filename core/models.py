import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.


class User(AbstractUser):
    GENDER_CHOICE = [
        ('male', u'男'),
        ('female', u'女'),
    ]
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称', default='')
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, default="female")
    address = models.CharField(max_length=100, default=u'')
    moblile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}".format(self.get_username())


class EmailVerifyRecord(models.Model):
    SEND_CHOICES = (
        ('regisgter', u"注册"),
        ('forget', u"找回密码"),
        ('update_email', u"修改邮箱"),
    )

    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(choices=SEND_CHOICES, max_length=20, verbose_name=u'验证码类型')
    send_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'发送时间')

    class Meta:
        verbose_name = u"邮件验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{code}({email})".format(code=self.code, email=self.email)


class Boss(models.Model):
    """
    Boss
    """
    boss_name = models.CharField(max_length=10, null=True, blank=True, verbose_name='boss昵称', help_text='boss昵称')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name="手机号", help_text="手机号")
    boss_level = models.CharField(max_length=11, null=True, blank=True, verbose_name="level", help_text="level")

    def __str__(self):
        return self.boss_name

    class Meta:
        db_table = 'boss'
        # permissions=(
        #     ("view_user", "cat view user"),
        # )

    def __str__(self):
        return "{}".format(self.boss_name)


# pageJson: 使用树模型
class PageJson(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = u'科室'
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return "{}".format(self.id)
