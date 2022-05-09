"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from sqlalchemy import *

from jinja_orm.server import db



if __name__ == '__main__':
    # db.create_all()
    db.drop_all()
    # student = StudentModel(name="张三")
    # print(student.courses)