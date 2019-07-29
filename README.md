### drf开发基础包
> 日常使用drf进行后端开发中，每次开发新项目就的做很多的工程基础配置操作，我觉得这样是没必要的，我们主要关注在业务的开发中，而不是每次都要做这些繁琐的基础操作，所以我把这些做了一个基础包，以后开发新项目就不需要做这些步骤了，可以直接进行业务的开发

#### 版本
- Python3.6
- Django2.X

#### DRF集成基础功能

- **认证**
- **跨域**
- **过滤器**
- **api文档**
- **分页**
- **日志**
- **扩展用户**
- **。。。**

#### 说明
在这个基础包里有一个用户增删改查的接口，即开即用，可以进行扩展


#### 安装部署
```
# 安装依赖包
pip install requirements.txt
# 修改数据库地址
修改opsweb/settings文件
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test002',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    },
}
#迁移数据库
python manger.py makemigrations
python manage.py migrate
#启动
python manage.py  runserver 0:8000
```

### frontend
[webpack参考](https://www.jianshu.com/p/937b2cc758c3)
```
./node_modules/.bin/webpack-cli --config webpack.config.js
```
