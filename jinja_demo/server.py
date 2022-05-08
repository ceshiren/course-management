"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session

from log_util import logger

from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

db_session: Session = db.session


@app.route("/courses", methods=["get"])
def get_course():
    """
    查询接口
    :return:
    """
    from course import CourseModel
    # 获取课程
    id = request.args.get("id")
    logger.info(f"接收到的参数: {id}")
    datas = []
    if id:
        data = CourseModel.get_filter(id=id)
        # logger.info(f"要查询的数据为===>{data}")
        print(f"要查询的数据为===>{data}")
        if data:
            datas = [{"id": data.id,
                      "name": data.name,
                      "desc": data.desc,
                      }]
    else:
        courses = CourseModel.get_all()
        logger.info(f"查询所有数据===>{courses}")
        # for course in courses:
        #     data = {"id":course.id,
        #              "name":course.name,
        #              "desc":course.desc
        #             }
        #     datas.append(data)
        datas = [{"id": course.id,
                  "name": course.name,
                  "desc": course.desc}
                 for course in courses]

    print(f"要返回的数据 ===>{datas}")
    # return {"code": 0, "msg": "success", "data": datas}
    return render_template('course_new.html', course_list=datas)


@app.route("/courses", methods=["post"])
def post_course():
    # 添加课程
    data = request.json
    logger.info(f"接收到的参数======> {data}")
    # id = int(data.get("id"))
    name = data.get("name")
    desc = data.get("desc")
    from course import CourseModel
    r = CourseModel.create(name, desc)
    if r:
        data = {"id": r, "name": name, "desc": desc}
        return {"code": 0, "msg": "success", "data": data}
    else:
        return {"code": 40001, "msg": "creat failed"}


@app.route("/courses", methods=["put"])
def put_course():
    # 修改课程
    data = request.json
    print(f"接收到的参数<====== {data}")
    id = int(data.get("id"))
    name = data.get("name")
    desc = data.get("desc")
    from course import CourseModel
    exists = CourseModel.get_filter(id=id)
    if exists:
        obj = CourseModel.update(id, name, desc)
        datas = [{
            "id": obj.id,
            "name": obj.name,
            "desc": obj.desc}]
        return {"code": 0, "msg": "success", "data": datas}
    else:
        return {"code": 40002, "msg": "course is not exists"}

@app.route("/courses", methods=["delete"])
def del_course():
    # 删除课程
    id = int(request.json.get("id"))
    from course import CourseModel
    exists = CourseModel.get_filter(id=id)
    if exists:
        CourseModel.delete(id=id)
        return {"code":0, "msg":"delete success"}
    else:
        return {"code":40002, "msg":"course is not exists"}

@app.route("/addCourse", methods=["get"])
def add_course():
    # return render_template("addCourse.html")
    return render_template("add_course_new.html")


@app.route("/editCourse/<course_id>/<course_name>/<course_desc>", methods=["get"])
def edit_course(course_id, course_name, course_desc):
    # return render_template("editCourse.html", course_id=course_id, course_name=course_name, course_desc=course_desc)
    return render_template("edit_course_new.html", course_id=course_id, course_name=course_name, course_desc=course_desc)

# 学员管理
@app.route("/student", methods=["GET"])
def get_student():
    stu_data = [
        {
            "stu_id": 1,
            "stu_name": "lily",
            "selectd_courses": [
                {
                    "course_id": 1,
                    "course_name": "测开21期",
                    "course_desc": "python 高级课程"
                },
                {
                    "course_id": 2,
                    "course_name": "测开22期",
                    "course_desc": "python 高级课程"
                }
            ]
        },
        {
            "stu_id": 2,
            "stu_name": "tom",
            "selectd_courses": [
                {
                    "course_id": 2,
                    "course_name": "测开22期",
                    "course_desc": "python 高级课程"
                },
                {
                    "course_id": 3,
                    "course_name": "就业3期",
                    "course_desc": "python 基础课程"
                },
            ]
        }
    ]
    # return render_template("student.html")
    return render_template("student_new.html", stu_data=stu_data)


if __name__ == '__main__':
    app.run(port=5008, debug=True)
