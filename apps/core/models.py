from django.db import models
# Create your models here.


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
