# blog
Simple blog system


## Core tech stack
* MySQL
* Flask
* SQLAlchemy
* Bootstrap


## Install
brew install mysql@5.7
brew link mysql
pip install mysql-python

注意，测试发现mysql-python只支持5.7。

## DB 操作
flask shell
db.create_all()
db.drop_all()

