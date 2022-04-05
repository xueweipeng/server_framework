from main import db


class PicFile(db.Model):
    # 定义表名
    __tablename__ = 'picfile'  # 定义表名
    # 定义对象
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(64), unique=True)
    timestamp = db.Column(db.Integer, unique=False)
    # 设置外键[用于查询一对多额情况]
    # us = db.relationship('User', backref='role', lazy='dynamic')

    # repr()方法类似于django的__str__,用于打印模型对象的字符串信息
    def __repr__(self):
        return 'PicFile:%s, %s, %s' % self.id, self.path, self.timestamp
