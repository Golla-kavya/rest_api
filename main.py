from flask import Flask,jsonify
todo=Flask(__name__)
students=[
    {
        "id":1,
        "name":"bujji",
        "age":18
    },
    {
        "id":2,
        "name":"chitti",
        "age":19
    },
    {
        "id":3,
        "name":"chinni",
        "age":20
    }
]
@todo.route('/students-list')
def get_student_list():
    return jsonify(students)

if __name__=='__main__':
    todo.run(
        host='127.0.0.1',
        port=5010,
        debug=True
    )