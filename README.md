# SBlog
简单的博客系统，用于练习。


## 组件
* MySQL
* Flask
* SQLAlchemy
* Bootstrap


## 安装
```
brew install mysql@5.7
brew link mysql
pip install mysql-python
```

注意，测试发现mysql-python只支持5.7。

## VSCode
禁止部分pylint的warning：
https://stackoverflow.com/questions/4341746/how-do-i-disable-a-pylint-warning

比如禁止sqlalchemy的error，可以:
```
ignore-modules=flask_sqlalchemy
```

快捷键：
1. 光标跳转: ctrl+-, ctrl+shift+-
2. 查找文件cmd+p
3. 查找buffer： ctrl+tab
参考:
https://code.visualstudio.com/docs/editor/editingevolved


## 数据库操作
```
flask shell
db.create_all()
db.drop_all()
```

## 运行
```
export FLASK_APP=blog.py
flask run
```

## uWSGI
```
# Enter project path
uwsgi --ini runtime/blog.ini
```
