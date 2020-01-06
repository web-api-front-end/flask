from flask import Blueprint, request
from model import User

user_opt = Blueprint('user_opt', __name__)


@user_opt.route('/', methods=['GET', 'POST'])
def create_user():
    '''
    创建博客文章
    '''
    if request.method == 'GET':
        users = User.query.all()
        # 渲染博文列表页面目标文件，传入blogs参数
        return "render_template('list_blogs.html', blogs=users)"
    else:
        # 从表单请求体中获取请求数据
        title = request.form['title']
        text = request.form['text']

        # 创建一个博文对象
        user = User(title=title, text=text)
        db.session.add(user)
        # 必须提交才能生效
        db.session.commit()
        # 创建完成之后重定向到博文列表页面
        return "redirect('/blogs')"


@user_opt.route('/<id>', methods=['GET', 'DELETE'])
def query_user(id):
    '''
    查询博文详情、修改、删除博文
    '''
    if request.method == 'GET':
        # 到数据库查询博文详情
        user = User.query.filter_by(id=id).first_or_404()
        # 渲染博文详情页面
        return "render_template('query_blog.html', blog=user)"
    elif request.method == 'PUT':
        '''
            更新博文
            '''
        # 获取请求的博文标题和正文
        title = request.form['title']
        text = request.form['text']

        # 更新博文
        user = User.query.filter_by(id=id).update({'title': title, 'text': text})
        # 提交才能生效
        db.session.commit()
        # 修改完成之后重定向到博文详情页面
        return "redirect('/blogs/{id}'.format(id=id))"
    else:
        # 删除博文
        user = User.query.filter_by(id=id).delete()
        # 提交才能生效
        db.session.commit()
        # 返回204正常响应，否则页面ajax会报错
        return '', 204
