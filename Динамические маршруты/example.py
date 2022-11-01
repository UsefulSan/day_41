from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/courses/<course_id>')
def courses(course_id):
    return f'Course id: {course_id}'

@app.route('/lessons/<lesson_id>')
def lessons(lesson_id):
    return f'Lesson id: {lesson_id}'




@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        return 'Hello from POST /users'
    return 'Hello from GET /users'