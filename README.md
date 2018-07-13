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
