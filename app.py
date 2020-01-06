# coding:utf-8
# Hello World
from __future__ import unicode_literals

import os

from flask import Flask

# 创建应用程序对象
from flask_sqlalchemy import SQLAlchemy

from blog.views import blog_opt
from user.views import user_opt

app = Flask(__name__)

# 注册蓝图，并指定其对应的前缀（url_prefix）
app.register_blueprint(user_opt, url_prefix="/users")
app.register_blueprint(blog_opt, url_prefix="/blogs")


# 获取当前目录的绝对路径
basedir = os.path.abspath(os.path.dirname(__file__))
# sqlite数据库文件存放路径
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'app.sqlite')
# 创建数据库对象
db = SQLAlchemy(app)

@app.route('/')
def hello():
    '''
    hello请求
    '''
    # 直接返回字符串
    return 'Hello, Flask World!'
        
if __name__ == '__main__':
    # 以debug模式启动程序
    app.run(host="127.0.0.1", port=5000, debug=True)