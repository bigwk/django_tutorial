# django 小项目

## update
* 使用`django template`

* 优化配置文件

设置`django settings`从配置文件读取。
```shell script
cp config.ini.example config.ini
```

* 修复`admin`异常退出

安装`django 2.2`
```shell script
pip install django==2.2
```

* `admin` 异常退出

访问`admin/`的时候服务异常退出，经排查后应该是`python`版本的问题。
解决方案是升级`python`版本到`3.7.x`，`x>=1`

[Python 3.7 crashes](https://code.djangoproject.com/ticket/31067)