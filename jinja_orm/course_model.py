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

# 中间表
course_student_rel = db.Table(
    # 中间表的名称
    'course_student_rel',
    # 其中一张表的描述，作为一个外键指向测试用例表的id
    Column('course_id', Integer,
           ForeignKey('course.id'),
           primary_key=True),
    # 其中一张表的描述，作为一个外键指向测试用例表的id
    Column('student_id', Integer,
           ForeignKey('student.id'),
           primary_key=True)
)

class MainTeacher(db.Model):
    __tablename__ = "main_teacher"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)


class StudentModel(db.Model):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    teacher_id = db.Column(Integer, ForeignKey("main_teacher.id"))
    teacher_obj = db.relationship("MainTeacher", backref='student_obj')
    # ===========一对多
    # 分别创建数据
    # db.create_all()
    # db.drop_all()
    # t1 = MainTeacher(name="飞儿老师")
    # t2 = MainTeacher(name="西西老师")
    # s1 = StudentModel(name="张三", teacher_id=1)
    # s2 = StudentModel(name="李四", teacher_id=1)
    # s3 = StudentModel(name="王五", teacher_id=1)
    # db.session.add_all([s3])
    # db.session.commit()
    # db.session.close()
    # s = StudentModel.query.all()
    # s[0].teacher_obj.name = "飞儿2"
    # db.session.commit()
    # db.session.close()
    # s = StudentModel.query.all()
    # print(s[0].teacher_obj.name)
    # print(MainTeacher.query.all()[0].student_obj[0].name)



class CourseModel(db.Model):
    # 表名
    __tablename__ = "course"
    # 用例ID 用例的唯 一标识
    id = db.Column(Integer, primary_key=True)
    # 用例的标题 或者文件名,限定 80个字符 ，不为空
    name = db.Column(String(80), nullable=False)
    # 备注
    desc = db.Column(String(120))
    student_objs = db.relationship("StudentModel",
                                   secondary=course_student_rel,
                                   backref="course_objs")

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
# =============中间表


# if __name__ == '__main__':
    # db.create_all()
    # db.drop_all()
    # c1 = CourseModel(name="大学英语", desc="必修")
    # c2 = CourseModel(name="高数", desc="必修")
    # c3 = CourseModel(name="计算机网络", desc="必修")
    # s1 = StudentModel(name="张三")
    # s2 = StudentModel(name="李四")
    # s3 = StudentModel(name="王五")
    # db.session.add_all([c1,c2,c3, s1,s2,s3])
    # db.session.commit()
    # db.session.close()



    # CourseModel.query.all()[0].student_objs = student[0:2]
    # db.session.commit()
    # db.session.close()
