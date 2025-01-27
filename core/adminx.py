import xadmin
from xadmin import views

# from .models import UserProfile
from .models import PageJson, EmailVerifyRecord


class BaseSetting(object):
    """
    主题功能开启
    """
    enable_themes = True
    # 需要开通代理，访问谷歌
    use_bootswatch = True


class GlobalSettings(object):
    """
    title:
    footer:
    """
    site_title = "adminx"
    site_footer = "adminx"
    # 收起菜单
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    """
    默认模型显示模式:
    1.search_fields:    #搜索范围
    2.list_display:     #列表显示
    3.list_filter:      #列表过滤
    4.ordering:         #默认排序,'-':倒序,从大到小
    5.readonly_fields   # 直接编辑
    6.refresh_times     # 刷新秒数
    7.list_editable     # 直接编辑
    """
    list_display = ['id', 'code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    ordering = ['-id']
    readonly_fields = ['email', 'send_type', 'send_time']
    refresh_times = [3, 5]
    list_editable = ['code']


class PageJsondAdmin(object):
    """
    默认模型显示模式:
    1.search_fields:    #搜索范围
    2.list_display:     #列表显示
    3.list_filter:      #列表过滤
    4.ordering:         #默认排序,'-':倒序,从大到小
    5.readonly_fields   # 直接编辑
    6.refresh_times     # 刷新秒数
    7.list_editable     # 直接编辑
    """
    list_display = ['id', 'name', 'level', 'parent']
    ordering = ['id', 'level']
    refresh_times = [3, 5]
    search_fields = ['name']
    list_filter = ['level']

# 将Xadmin全局管理器与我们的view绑定注册。
xadmin.site.register(views.BaseAdminView, BaseSetting)
# 将头部与脚部信息进行注册:
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(PageJson, PageJsondAdmin)
