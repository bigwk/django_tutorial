# django 小项目

## update
* admin 异常退出

访问`admin/`的时候服务异常退出，经排查后应该是`python`版本的问题。
解决方案是升级`python`版本到`3.7.x`，`x>=1`

[Python 3.7 crashes](https://code.djangoproject.com/ticket/31067)