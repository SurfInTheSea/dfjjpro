from django.db import models


class User(models.Model):
    name = models.CharField('用户名', max_length=128, unique=True)
    password = models.CharField('密码', max_length=256)
    money = models.FloatField('用户余额', default=0)
    c_time = models.DateTimeField('添加时间', auto_now_add=True)
    realName = models.CharField('真实姓名', max_length=128, default='')
    bank = models.CharField('银行', max_length=128, default='')
    bank_details = models.CharField('开户行', max_length=256, default='')
    bank_acount = models.CharField('卡号', max_length=256, default='')
    pay_name = models.CharField('利息账户', max_length=128, default='')
    FakeMoney = models.FloatField('赠送金额（无法提现）', default=0)
    IsUserHaveFakeMoney = models.BooleanField('有无彩金', default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'


class ProgramInfo(models.Model):
    name = models.CharField('项目名称', max_length=128, unique=True)  # 项目名称
    programText = models.TextField('项目简介', )  # 项目简介
    minPay = models.IntegerField('最小买入值', )
    payBack = models.FloatField('利率%', )
    payDay = models.IntegerField('周期（天）', )
    c_time = models.DateTimeField('创立时间', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('DFJJ:programDetails', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '项目'
        verbose_name_plural = '项目名称'


class OperatingInfo(models.Model):
    name = models.CharField('用户名', max_length=128, unique=True, null=True, blank=True)
    money = models.FloatField('变动之前余额', default=0, null=True, blank=True)
    pay_name = models.CharField('利息账户', max_length=128, default='')
    program_name = models.CharField('项目名称', max_length=128, null=True, blank=True)  # 项目名称
    program_minPay = models.IntegerField('最小买入值', null=True, blank=True)  # 项目的最低金额
    program_payBack = models.FloatField('利率%', null=True, blank=True)  # 项目的利息
    payDay = models.IntegerField('周期（天）', null=True, blank=True)
    program_count = models.IntegerField('买入数量', null=True, blank=True)  # 该会员此次购入数量
    mone_done = models.FloatField('变动之后余额', default=0, null=True, blank=True)  # 会员结算后的金额
    payMoney = models.FloatField('应该获得的利润', default=0, null=True, blank=True)
    c_time = models.DateTimeField('发生时间', auto_now=True, null=True, blank=True)
    out_time = models.DateTimeField('获得利息时间', null=True, blank=True)  # 出利息的时间

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '变更记录'
        verbose_name_plural = '变更记录'
'''
class ActivityInfo(models.Model):
    name = models.CharField('活动名称', max_length=128, unique=True, null=True, blank=True)
    activityText = models.TextField('活动简介', null=True, blank=True)
    activityMoney = models.FloatField('活动金额', default=0, null=True, blank=True)
    c_time = models.DateTimeField('发布时间', auto_now=True, null=True, blank=True)
    ActivityEndTime = models.DateTimeField('活动结束时间', auto_now=True, null=True, blank=True)
    ActivityMinMoney = models.IntegerField('最小购入金额', default=0, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '活动简介'
        verbose_name_plural = '活动简介'

'''

