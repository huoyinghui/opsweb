### xadmin

[参考](https://blog.csdn.net/weixin_34194551/article/details/88065632)
[install](https://github.com/sshwsfc/xadmin)


```
pipenv install https://codeload.github.com/sshwsfc/xadmin/zip/django2
pip install git+git://github.com/sshwsfc/xadmin.git@django2
```

settings.py
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'leads',          # 添加leads app
    'rest_framework', # 添加rest framework
    'xadmin',         # 添加 xadmin
    'crispy_forms',   # 添加 xadmin

]
```

urls.py
```
from django.urls import path, include
import xadmin

urlpatterns = [
    path('', include('leads.urls')),
    path('xadmin/', xadmin.site.urls),
]
```

