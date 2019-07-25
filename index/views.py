from django.shortcuts import render, redirect
from . import models
from .forms import UserForm, RegisterForm
import hashlib
from django.contrib import messages
import datetime

from django.utils.timezone import now, timedelta


# from django.utils import timezone
# from time import datetime

def hash_code(s, salt='python-django-hash-0451392aa##'):  # 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


def index(request):
    programInfos = models.ProgramInfo.objects.all()
    return render(request, 'index/index.html', {'programInfos': programInfos})


# return render(request, 'DFJJ/index.html',  {'programInfos':programInfos} )


def login(request):
    if request.session.get('is_login', None):
        return redirect("/index/")
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == hash_code(password):  # 哈希值和数据库内的值进行比对
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    request.session['money'] = user.money
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login/login.html', locals())

    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = hash_code(password1)  # 使用加密密码
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")


def indexText(request):
    return render(request, 'index/index-self.html', context={
        "loginState": "F",
        "index": 0,
        "code": "000",
        "productInfoVo":
            [
                {"baseYields": "6.0", "yields": "6.0", "timeLong": "90", "minInvest": 100.00, "maxInvest": 90000000.00,
                 "restAmount": "273858.83", "startTime": "null", "endTime": "null", "productCode": "Q3-190117150904512",
                 "totalAmount": "null", "productName": "季账户-3个月", "createTime": "null", "url": "null",
                 "productPackageCode": "190117150904512-778", "productType": "Q3", "extraProfit": "F",
                 "isShowGreen": "null", "upProfit": "", "maxProfit": "6.0", "isShowActivityInfo": "F",
                 "activityInfo": "", "extraInfo": "", "isShowextraInfo": "F", "isShow": "T", "startDateAPP": "null",
                 "startTimeAPP": "null", "recommendCount": "null", "longtimeMarkFlag": "null",
                 "longtimeMarkContent": "null", "yieldMarkFlag": "null", "yieldMarkContent": "null", "assistMsg": "",
                 "accountSign": "null", "investCount": "null", "productSubType": "null", "isDepository": "1",
                 "accountType": "null", "isSellout": "F", "buttonDesc": "null", "reamarks": "", "fbProductType": "0",
                 "mdesc": "null", "isUser": "F", "hdesc": "null"},
                {"baseYields": "9.4", "yields": "9.4", "timeLong": "365", "minInvest": 1000.00, "maxInvest": 2000000.00,
                 "restAmount": "1148905.43", "startTime": "null", "endTime": "null",
                 "productCode": "T365-190628112609101", "totalAmount": "null", "productName": "限时特供365天",
                 "createTime": "null", "url": "null", "productPackageCode": "190628112609101-2", "productType": "T",
                 "extraProfit": "F", "isShowGreen": "null", "upProfit": "", "maxProfit": "", "isShowActivityInfo": "F",
                 "activityInfo": "", "extraInfo": "", "isShowextraInfo": "F", "isShow": "T", "startDateAPP": "null",
                 "startTimeAPP": "null", "recommendCount": "null", "longtimeMarkFlag": "null",
                 "longtimeMarkContent": "null", "yieldMarkFlag": "null", "yieldMarkContent": "null", "assistMsg": "",
                 "accountSign": "null", "investCount": "null", "productSubType": "null", "isDepository": "1",
                 "accountType": "null", "isSellout": "F", "buttonDesc": "null", "reamarks": "", "fbProductType": "0",
                 "mdesc": "null", "isUser": "F", "hdesc": "null"},
                {"baseYields": "4.5", "yields": "4.5", "timeLong": "1", "minInvest": 100.00, "maxInvest": 50000.00,
                 "restAmount": "112801.96", "startTime": "null", "endTime": "null", "productCode": "M190117151824811",
                 "totalAmount": "null", "productName": "月账户", "createTime": "null", "url": "null",
                 "productPackageCode": "190117151824811-772", "productType": "M", "extraProfit": "F",
                 "isShowGreen": "F", "upProfit": "0.5", "maxProfit": "8.5", "isShowActivityInfo": "F",
                 "activityInfo": "", "extraInfo": "", "isShowextraInfo": "F", "isShow": "T", "startDateAPP": "null",
                 "startTimeAPP": "null", "recommendCount": "null", "longtimeMarkFlag": "null",
                 "longtimeMarkContent": "null", "yieldMarkFlag": "null", "yieldMarkContent": "null", "assistMsg": "",
                 "accountSign": "null", "investCount": "null", "productSubType": "null", "isDepository": "1",
                 "accountType": "null", "isSellout": "F", "buttonDesc": "null", "reamarks": "", "fbProductType": "0",
                 "mdesc": "4%起，逐月涨0.5%，30天后每月可申请转让1次", "isUser": "F", "hdesc": "null"},
                {"baseYields": "12.0", "yields": "12.0", "timeLong": "21", "minInvest": 100.00, "maxInvest": 30000.00,
                 "restAmount": "352577.02", "startTime": "null", "endTime": "null",
                 "productCode": "T21-FB190117151528287", "totalAmount": "null", "productName": "新手专享21天",
                 "createTime": "null", "url": "null", "productPackageCode": "190117151528287-376", "productType": "T",
                 "extraProfit": "F", "isShowGreen": "null", "upProfit": "", "maxProfit": "", "isShowActivityInfo": "F",
                 "activityInfo": "", "extraInfo": "", "isShowextraInfo": "F", "isShow": "T", "startDateAPP": "null",
                 "startTimeAPP": "null", "recommendCount": "null", "longtimeMarkFlag": "null",
                 "longtimeMarkContent": "null", "yieldMarkFlag": "null", "yieldMarkContent": "null", "assistMsg": "",
                 "accountSign": "null", "investCount": "null", "productSubType": "null", "isDepository": "1",
                 "accountType": "null", "isSellout": "F", "buttonDesc": "null", "reamarks": "新用户出借一次</br>上限3万元",
                 "fbProductType": "N21", "mdesc": "null", "isUser": "F", "hdesc": "null"},
                {"baseYields": "8.0", "yields": "8.0", "timeLong": "90", "minInvest": 100.00, "maxInvest": 20000.00,
                 "restAmount": "205827.72", "startTime": "null", "endTime": "null",
                 "productCode": "T90-FB190117151749370", "totalAmount": "null", "productName": "新手专享90天",
                 "createTime": "null", "url": "null", "productPackageCode": "190117151749370-364", "productType": "T",
                 "extraProfit": "F", "isShowGreen": "null", "upProfit": "", "maxProfit": "", "isShowActivityInfo": "F",
                 "activityInfo": "", "extraInfo": "", "isShowextraInfo": "F", "isShow": "T", "startDateAPP": "null",
                 "startTimeAPP": "null", "recommendCount": "null", "longtimeMarkFlag": "null",
                 "longtimeMarkContent": "null", "yieldMarkFlag": "null", "yieldMarkContent": "null", "assistMsg": "",
                 "accountSign": "null", "investCount": "null", "productSubType": "null", "isDepository": "1",
                 "accountType": "null", "isSellout": "F", "buttonDesc": "null", "reamarks": "出借1万元</br>期望回报197.26元",
                 "fbProductType": "N90", "mdesc": "null", "isUser": "F", "hdesc": "null"},
                {"baseYields": "10.0", "yields": "10.0", "timeLong": "365", "minInvest": 100.00, "maxInvest": 10000.00,
                 "restAmount": "616239.82", "startTime": "null", "endTime": "null",
                 "productCode": "T365-FB190117151640326", "totalAmount": "null", "productName": "新手专享365天",
                 "createTime": "null", "url": "null", "productPackageCode": "190117151640326-209", "productType": "T",
                 "extraProfit": "F", "isShowGreen": "null", "upProfit": "", "maxProfit": "", "isShowActivityInfo": "F",
                 "activityInfo": "", "extraInfo": "", "isShowextraInfo": "F", "isShow": "T", "startDateAPP": "null",
                 "startTimeAPP": "null", "recommendCount": "null", "longtimeMarkFlag": "null",
                 "longtimeMarkContent": "null", "yieldMarkFlag": "null", "yieldMarkContent": "null", "assistMsg": "",
                 "accountSign": "null", "investCount": "null", "productSubType": "null", "isDepository": "1",
                 "accountType": "null", "isSellout": "F", "buttonDesc": "null", "reamarks": "出借1万元</br>期望回报1000.0元",
                 "fbProductType": "N365", "mdesc": "null", "isUser": "F", "hdesc": "null"},
                {"baseYields": "8.5", "yields": "8.5", "timeLong": "365", "minInvest": 100.00, "maxInvest": 99999999.99,
                 "restAmount": "1126239.98", "startTime": "null", "endTime": "null",
                 "productCode": "Y12-190221144847577", "totalAmount": "null", "productName": "年账户-1年",
                 "createTime": "null", "url": "null", "productPackageCode": "190221144847577-627", "productType": "Y",
                 "extraProfit": "F", "isShowGreen": "null", "upProfit": "", "maxProfit": "8.5",
                 "isShowActivityInfo": "F", "activityInfo": "", "extraInfo": "", "isShowextraInfo": "F", "isShow": "T",
                 "startDateAPP": "null", "startTimeAPP": "null", "recommendCount": "null", "longtimeMarkFlag": "null",
                 "longtimeMarkContent": "null", "yieldMarkFlag": "null", "yieldMarkContent": "null", "assistMsg": "",
                 "accountSign": "null", "investCount": "null", "productSubType": "null", "isDepository": "1",
                 "accountType": "null", "isSellout": "F", "buttonDesc": "null", "reamarks": "", "fbProductType": "0",
                 "mdesc": "null", "isUser": "F", "hdesc": "null"}
            ]
    })


def base(request):
    return render(request, 'base.html')


def newguide(request):
    if not request.session.get('is_login', None):
        messages.success(request, "请先登录，5000新人红包在等您哦～～")
        return redirect("/login/")
    if request.method == "POST":
        name = request.session['user_name']
        # messages.success(request, "POST:提交成功;用户名" + name + "")
        if name is not None:
            UserInfo = models.User.objects.get(name=name)

            if UserInfo.IsUserHaveFakeMoney:
                UserInfo.FakeMoney = UserInfo.FakeMoney + 5000
                UserInfo.money = + UserInfo.FakeMoney
                UserInfo.IsUserHaveFakeMoney = False
                UserInfo.save()
                messages.success(request, "提交成功;用户名=" + name + ";虚拟账户=" + str(UserInfo.FakeMoney) + "")
            else:
                messages.success(request, "该活动只能参与一次哦")
        return render(request, 'index/newguide.html')



    return render(request, 'index/newguide.html')


def trust(request):
    return render(request, 'index/trust.html')


def infomation(request):
    return render(request, 'index/infomation.html')


# 项目名称(name)---项目简介(programText)---最小买入值(minPay)---利率(payBack)---周期（天）(payDay)
def maintz(request):
    # models.ProgramInfo.objects.all()
    # print(models.ProgramInfo.objects.all())
    program_infos = models.ProgramInfo.objects.all()

    print(program_infos)

    # {'program_infos': user_list}

    return render(request, 'index/maintz.html', {'program_infos': program_infos})


def programDetails(request, pk):
    programDetail = models.ProgramInfo.objects.get(id=pk)
    # print(pk)
    print(programDetail)
    return render(request, 'index/programDetails.html', {'programDetail': programDetail})


def buyProgramDetails(request, pk):
    if not request.session.get('is_login', None):
        return redirect("/login/")

    if request.method == "POST":
        programDetail = models.ProgramInfo.objects.get(id=pk)
        personalInfo = models.User.objects.get(name=request.session['user_name'])

        program_count = request.POST.get('program_count', None)
        try:
            f = float(program_count)
        except ValueError:
            print('输入不是数字')
            messages.success(request, "请正确填写您需要购入的数量！")
            return redirect("/index/")
        # print(programDetail, personalInfo, program_count)

        OperatingOne = models.OperatingInfo.objects.create()
        OperatingOne.name = personalInfo.name
        OperatingOne.money = personalInfo.money
        OperatingOne.pay_name = personalInfo.pay_name
        OperatingOne.payDay = programDetail.payDay
        OperatingOne.program_name = programDetail.name
        OperatingOne.program_minPay = programDetail.minPay
        OperatingOne.program_payBack = programDetail.payBack
        OperatingOne.program_count = program_count
        # OperatingOne.payDay = programDetail.payDay
        if personalInfo.money < (float(programDetail.minPay) * float(program_count)):
            print('余额不足！')
            messages.success(request, "余额不足！请及时到充值渠道充值哦")
            return redirect("/index/")
        OperatingOne.mone_done = personalInfo.money - float(programDetail.minPay) * float(program_count)
        OperatingOne.payMoney = round((float(programDetail.minPay) * float(program_count)), 2)
        now = datetime.datetime.now()
        OperatingOne.out_time = now + datetime.timedelta(days=programDetail.payDay)
        print(
            OperatingOne.name, OperatingOne.money, OperatingOne.pay_name, OperatingOne.program_name,
            OperatingOne.program_minPay, OperatingOne.program_payBack, OperatingOne.program_count,
            OperatingOne.mone_done,
            OperatingOne.out_time
        )
        if OperatingOne.name and OperatingOne.money and OperatingOne.pay_name and OperatingOne.program_name and OperatingOne.program_minPay and OperatingOne.program_payBack and OperatingOne.program_count and OperatingOne.mone_done:
            OperatingOne.save()
        models.User.objects.filter(name=request.session['user_name']).update(money=OperatingOne.mone_done)
        print('提款时间：', OperatingOne.out_time)
        print('账户余额：', OperatingOne.mone_done)
        print('购买产品成功！')
        # *"+ OperatingOne.program_count +"="+ OperatingOne.program_minPay * OperatingOne.program_minPay +"
        messages.success(request,
                         "恭喜您，成功购入" + OperatingOne.program_name + "，总计:" + str(OperatingOne.program_minPay) + "*" + str(
                             OperatingOne.program_count) + "="
                         + str(OperatingOne.program_minPay * OperatingOne.program_count) + "元")
        return redirect("/index/")

    programDetail = models.ProgramInfo.objects.get(id=pk)
    personalInfo = models.User.objects.get(name=request.session['user_name'])
    # personalInfo =models.User.objects.filter(name=username)
    print(programDetail)
    print(personalInfo)

    return render(request, 'index/buyProgramDetails.html',
                  {'programDetail': programDetail, 'personalInfo': personalInfo})


def elseinfo(request):
    return render(request, 'DFJJ/elseinfo.html')


def userCenter(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")
    user = models.User.objects.filter(name=request.session['user_name']).get()
    FakeMoney = user.FakeMoney
    print(FakeMoney)
    now = datetime.datetime.now()
    OperatingOnes = models.OperatingInfo.objects.filter(name=request.session['user_name'], out_time__gt=now)
    payToday = 0
    moneyTotall = 0
    for OperatingOne in OperatingOnes:
        print(OperatingOne.name, OperatingOne.money, OperatingOne.pay_name, OperatingOne.program_name,
              OperatingOne.program_minPay, OperatingOne.program_payBack, OperatingOne.program_count,
              OperatingOne.mone_done,
              OperatingOne.out_time)
        payToday += OperatingOne.program_minPay * OperatingOne.program_payBack * OperatingOne.program_count / 100
        moneyTotall += OperatingOne.program_minPay * OperatingOne.program_count
        print(payToday)
    moneyTotall += user.money
    moneyNow = user.money
    print(moneyTotall)

    return render(request, 'index/userCenter.html',
                  {'payToday': round(payToday, 2),
                   'moneyTotall': moneyTotall,
                   'moneyNow': moneyNow, 'FakeMoney': FakeMoney})


'''
    if not request.session.get('is_login', None):
        return redirect("/login/")
    user = models.User.objects.get(name=request.session['user_name'])
    print(user.money)
    OperatingInfo = models.OperatingInfo
    now = datetime.datetime.now()
    start = now - datetime.timedelta(hours=23, minutes=59, seconds=59)
    Operatings = OperatingInfo.objects.filter(out_time__gt = start).getall()
    accountAll = 0
    for Operating in Operatings:
        accountAll += Operating.program_minPay * Operating.program_count
    print(accountAll)
    request.session['accountAll'] = accountAlls
'''


def banckAndaccount(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")

    if request.method == "POST":
        realName = request.POST.get('realName', None)
        bank = request.POST.get('bank', None)
        bank_details = request.POST.get('bank_details', None)
        bank_acount = request.POST.get('bank_acount', None)
        pay_name = request.POST.get('pay_name', None)

        if realName and bank and bank_details and bank_acount and pay_name:
            # user.objects.filter(pk=some_value).update(field1='some value')
            # user_id = request.session['user_id']
            user = models.User
            # print(user)
            # print(type(user))
            # print(user.money)
            # print(realName, bank, bank_details, bank_acount, pay_name)
            user.objects.filter(name=request.session['user_name']).update(realName=realName, bank=bank,
                                                                          bank_details=bank_details,
                                                                          bank_acount=bank_acount, pay_name=pay_name)
            # user = models.User.objects.get(name=request.session['user_name'])
            # user.objects.filter(id=user.id).update(
            # realName=realName, bank=bank, bank_details=bank_details, bank_acount=bank_acount, pay_name=pay_name)
            messages.success(request, "改动成功")
            return redirect("/userCenter/")

        return render(request, 'index/banckAndaccount.html')

    user = models.User.objects.get(name=request.session['user_name'])
    request.session['money'] = user.money

    request.session['realName'] = user.realName
    request.session['bank'] = user.bank
    request.session['bank_details'] = user.bank_details
    request.session['bank_acount'] = user.bank_acount
    request.session['pay_name'] = user.pay_name

    return render(request, 'index/banckAndaccount.html')


def personalProgramDetails(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")
    # now =datetime.datetime.now()
    # print(request.session['user_name'])
    start = now().date()
    end = start + timedelta(days=1)
    # personalProgramDetails = models.OperatingInfo.objects.all().filter(out_time__range=(start, end))
    personalProgramDetails = models.OperatingInfo.objects.all().filter(name=request.session['user_name'],
                                                                       out_time__gt=start)
    # print(personalProgramDetails)
    if personalProgramDetails:
        print('Hello')
    else:
        print('Goodbye')
    for personalProgramDetail in personalProgramDetails:
        # personalProgramDetail = models.OperatingInfo
        print(
            personalProgramDetail.name,
            personalProgramDetail.money,
            personalProgramDetail.pay_name,
            personalProgramDetail.program_name,
            personalProgramDetail.program_minPay,
            personalProgramDetail.program_payBack,
            personalProgramDetail.program_count,
            personalProgramDetail.mone_done,
            personalProgramDetail.c_time,
            personalProgramDetail.out_time

        )

    # profit = float(programDetail.minPay)  / 100 * float(program_count) * float(OperatingOne.payDay)
    return render(request, 'index/personalProgramDetails.html', {'personalProgramDetails': personalProgramDetails})


def register1(request):
    return render(request, 'login/register1.html', {})




