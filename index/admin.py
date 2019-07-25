from django.contrib import admin
from . import models
# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ('name', 'password', 'money', 'realName','bank', 'bank_details', 'bank_acount', 'pay_name', 'c_time')
	actions_on_top =True
	actions_on_bottom = True
	actions_selection_counter = True
	empty_value_display = ' -空白- '
	search_fields = ('name', 'money', )

class ProgramInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'programText', 'minPay', 'payBack', 'payDay', 'c_time')
    #list_display = ('name', 'sex', 'age', 'TEL', 'member_type')
    actions_on_top =True
    actions_on_bottom = True
    actions_selection_counter = True
    empty_value_display = ' -空白- '
    #list_editable = ['minPay', 'payBack', 'payDay',]
    search_fields = ('name', 'payBack', )


class ProgramOperatingInfo(admin.ModelAdmin):
	list_display = ('id', 'c_time', 'name', 'money', 'program_name', 'program_minPay', 'payDay', 'program_payBack', 'program_count', 'payMoney', 'mone_done', 'out_time')
	actions_selection_counter = True
	empty_value_display = ' -空白- '
	list_per_page = 200
	search_fields = ('out_time', )


class ProgramInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'programText', 'minPay', 'payBack', 'payDay', 'c_time')
    #list_display = ('name', 'sex', 'age', 'TEL', 'member_type')
    actions_on_top =True
    actions_on_bottom = True
    actions_selection_counter = True
    empty_value_display = ' -空白- '
    #list_editable = ['minPay', 'payBack', 'payDay',]
    search_fields = ('name', 'payBack', )


class ProgramactivityInfo(admin.ModelAdmin):
	list_display = ('name', 'activityText', 'activityMoney', 'activityStayTime', 'c_time')
	actions_on_top = True
	actions_on_bottom = True
	actions_selection_counter = True
	empty_value_display = ' -空白- '
	search_fields = ('name', )




admin.site.site_header = '大发基金后台管理'
admin.site.site_title = '大发基金'

admin.site.register(models.User, UserAdmin)
admin.site.register(models.ProgramInfo, ProgramInfoAdmin)
admin.site.register(models.OperatingInfo, ProgramOperatingInfo)
admin.site.register(models.activityInfo, ProgramactivityInfo)





'''
from django.contrib import admin
from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

# 把新增的 PostAdmin 也注册进来
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
'''