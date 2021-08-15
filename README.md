# FlaskCMS

## 项目介绍

FlaskCMS是基于一款基于Flask的CMS系统，基于该系统，可以方便的的搭建自己的内容管理系统或者博客系统。

## 软件架构

### 软件架构说明

### 遗留问题

1、联合查询post，post author，category查询异常 2、鉴权问题

## 安装教程

### 创建数据库表结构

```bat
set FLASK_APP=manage.py
flsk db init
flask db migrate
flask db upgrade
```

### 添加默认数据

在PostgreSQL中执行init_db.sql的语句，创建默认数据

## 使用说明

### 使用JIJA2模板模式

按照__init__.py文件中的描述，打开注册蓝图的注释，然后将flask-restful相关的内容注释，然后执行运行命令：

```bat 
set FLASK_APP=manage.py
flask run
```

### 前后端分离模式

默认使用前后端分离模式，启动程序命令如下：

```bat 
set FLASK_APP=manage.py
flask run
```

## 参与贡献

1. Fork 本仓库
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request tee 封面人物是一档用来展示 Gitee 会员风采的栏目 https://gitee.com/gitee-stars/