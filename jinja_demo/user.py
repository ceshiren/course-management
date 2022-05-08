"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/name/<string:name>', methods=['GET'])
def name(name):
    mydict = {
        "d1": 0,
        "d2": "d2_value"
    }
    mylist = [0, 1, 2, "l1"]
    return render_template('user.html', name=name, mydict=mydict, mylist=mylist)


@app.route('/if/<string:name>', methods=['GET'])
def if_demo(name):
    return render_template('if.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)