# 2019-Software-Engineering-Curriculum-Design

## 欢迎来到2019软件工程选课管理系统

## 使用方法 Usage

1. 下载或clone项目
```
git clone https://github.com/se-curriculum-design-group/2019-Software-Engineering-Curriculum-Design.git
```
2. 安装`pymysql`或`mysqlclient`，安装`django-simple-captcha`，用于生成验证码。
```
$ pip install pymysql
$ # or pip install mysqlclient # 我的机器报错不晓得为啥-_-!
$ pip install django-simple-captcha
```
3. 数据库中创建用户和数据库
```
$ mysql -uroot -p
Enter your password: xxxxxx
mysql> create database EMS;
mysql> create user 'EMS'@'localhost' identified by 'password';
mysql>  grant all on *.* to 'EMS'@'localhost';
mysql> flush privileges;
```
4. 用PyCharm打开内部EMS文件夹。删除backstage模块migrations文件夹下除`__init__.py`的文件。重新生成迁移文件。
```
$ python manage.py makemigrations backstage  # 重新生成迁移文件。
$ python manage.py migrate  # 模型迁移到数据库中
$ python manage.py runserver  # 运行服务
```
成功运行没有报错的话，打开 http://127.0.0.1:8000/ 访问。

## 目前已完成的工作

## 选课子系统—功能需求分析
- ![](https://github.com/Messiahhhh/2019-Software-Engineering-Curriculum-Design--/blob/New_Master/EMS/courseSelection/%E9%80%89%E8%AF%BE%E5%AD%90%E7%B3%BB%E7%BB%9F-%E5%8A%9F%E8%83%BD%E9%9C%80%E6%B1%82%E5%88%86%E6%9E%90.md)

## 选课子系统-原型设计
- ![](https://github.com/Messiahhhh/2019-Software-Engineering-Curriculum-Design--/blob/New_Master/EMS/courseSelection/%E9%80%89%E8%AF%BE%E5%AD%90%E7%B3%BB%E7%BB%9F%E5%8E%9F%E5%9E%8B%E8%AE%BE%E8%AE%A1.md)
