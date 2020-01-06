class Blog(db.Model):
    '''
    博文数据模型
    '''
    # 主键ID
    id = db.Column(db.Integer, primary_key=True)
    # 博文标题
    title = db.Column(db.String(100))
    # 博文正文
    text = db.Column(db.Text)

    def __init__(self, title, text):
        '''
        初始化方法
        '''
        self.title = title
        self.text = text
