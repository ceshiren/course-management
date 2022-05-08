"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

# 数据库操作
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *

# 数据库配置
from log_util import logger
from server import db


class CourseModel(db.Model):
    # 表名
    __tablename__ = "course"
    # 用例ID 用例的唯 一标识
    id = db.Column(Integer, primary_key=True)
    # 用例的标题 或者文件名,限定 80个字符 ，不为空
    name = db.Column(String(80), nullable=False)
    # 备注
    desc = db.Column(String(120))

    @classmethod
    def get_all(cls):
        course_datas = cls.query.all()
        return course_datas

    @classmethod
    def get_filter(cls,**kwargs):
        course_datas = cls.query.filter_by(**kwargs).first()
        return course_datas

    @classmethod
    def create(cls,name,desc):
        instance = cls(name=name, desc=desc)
        db.session.add(instance)
        db.session.commit()
        course_id = instance.id
        logger.debug(f"创建的课程 ID 为-->{course_id}")
        db.session.close()
        return course_id

    @classmethod
    def delete(cls,**kwargs):
        cls.query.filter_by(**kwargs).delete()
        db.session.commit()
        db.session.close()

    @classmethod
    def update(cls, id, name,desc):
        # cls.query.filter_by(**kwargs).delete()
        update_data = {"id":id,"name":name,"desc":desc}
        cls.query.filter_by(id=id).update(update_data)
        db.session.commit()
        db.session.close()
        updated_obj = cls.get_filter(id=id)
        return updated_obj


if __name__ == '__main__':
    # db.create_all()
    # db.drop_all()
    # 新增 ---- 一条数据
    # course1 = CourseModel(name="测开22期",
    #        desc="python 高级课程1")
    # db.session.add(course1)
    # db.session.commit()
    # # commit 之后 可以拿到这个对象的返回
    # print(course1.id, course1.name, course1.desc)
    # db.session.close()

    # 新增 ---- 多条数据
    # course4 = CourseModel(id=4, name="测开4期",
    #                  desc="python 高级课程")
    # course5 = CourseModel(id=5, name="就业5期",
    #                  desc="python 基础课程")
    # db.session.add(course4)
    # db.session.add(course5)
    # db.session.commit()
    # db.session.close()
    pass