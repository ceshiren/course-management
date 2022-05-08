"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from flask import Flask, request, render_template
app = Flask(__name__)

from data import courses


# 课程管理
@app.route("/courses", methods=["get"])
def get_course():
    # 获取课程
    course_id = request.args.get("course_id")
    print(course_id)
    datas = []
    if course_id:
        # 如果不为空，则返回对应的课程
        for course in courses:
            if int(course_id) == course.get("course_id"):
                datas.append(course)
    else:
        # 返回所有数据
        datas = courses
    # return  {"code":0,"msg":"get success","data":datas}
    # return render_template('course.html', course_list=datas)
    return render_template('course_new.html', course_list=datas)

@app.route("/courses", methods=["post"])
def post_course():
    # 添加课程
    course_data = request.json
    print(f"接收到的参数<====== {course_data}")
    course_id = int(course_data.get("course_id"))
    course_name = course_data.get("course_name")
    course_desc = course_data.get("course_desc")
    new_course = {
            "course_id": course_id,
            "course_name": course_name,
            "course_desc": course_desc,
            }
    # 判断是否有课程
    for course in courses:
        if course.get("course_id") == course_id:
            return {"code": 40001, "msg": "course id is exists"}

    courses.append(new_course)
    print(f"当前所有课程：{courses}")
    return {"code": 0, "msg": f"course id {course_id} success add."}


@app.route("/courses", methods=["put"])
def put_course():
    # 修改课程
    course_data = request.json
    print(f"接收到的参数<====== {course_data}")
    course_id = int(course_data.get("course_id"))
    course_name = course_data.get("course_name")
    course_desc = course_data.get("course_desc")
    update_course = {
        "course_id": course_id,
        "course_name": course_name,
        "course_desc": course_desc,
    }

    for course in courses:
        if course.get("course_id") == course_id:
            # 先删除，再添加
            print(f"需要更新的课程：{course}")
            courses.remove(course)
            courses.append(update_course)
            print(f"当前所有课程：{courses}")
            return {"code": 0, "msg": f"课程{course} 更新为 {update_course}"}
    return {"code": 40001, "msg": "course is not exists"}


@app.route("/courses", methods=["delete"])
def del_course():
    # 删除课程
    course_id = int(request.json.get("course_id"))
    for course in courses:
        if course.get("course_id") == course_id:
            print(f"删除课程：{course}")
            courses.remove(course)
            print(f"当前所有课程：{courses}")
            return {"code":0,"msg":"delete success"}
    return {"code": 40001, "msg": "course is not exists"}


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
            "select_course": [
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
    app.run(port=5008,debug=True)