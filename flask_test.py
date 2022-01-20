from flask import Flask, jsonify

app = Flask(__name__)

courses = [{"name": "Python Programming Certification",
                  'course id': "0",
                  'Description': "Python programming certification helps you learn"
                                 "python in the structured learning path with innovative "
                                 "out of the box projects matching the industry standards",
                  'price' : "visit Edureka.co to know more"},
                {'name': "Data Science With Python Certification",
                 'course id': "1",
                'Description': "Data science with python helps you master the data science "
                               "life cycle processes in a structured learning path",
                'price': "visit edureka.co to know more"},
                {'name' : "AI and Machine Learning Certification",
                 'course id' : "2",
                 'Description': "AI and ML certification will help you master AI/ML with "
                                "top notch projects like speechrecognition, chatbots, etc.",
                 'price': "visit edureka.co to know more"},
                {'name': "Natural Language Processing with Python Certification",
                 'course_id': "4",
                 'Description': "Natural Language Processing with Python course will take you through "
                                "of testing processing all the way up to classifying texts using ML/AI",
                 'price': "visit edureka.co to know more"}
          ]


@app.route('/')
def index():
    return "Welcome to the Course API"


@app.route("/courses", methods=['GET'])
def get():
    return jsonify({'Courses': courses})


@app.route("/courses/<int:course_id>", methods=['GET'])
def get_course(course_id):
    return jsonify({'course': courses[course_id]})


@app.route("/courses", methods=['POST'])
def create():
    course = {'name': "Natural Language Processing with Python Certification",
              'course_id': "4",
              'Description': "Natural Language Processing with Python course will take you through "
                             "of testing processing all the way up to classifying texts using ML/AI",
              'price': "visit edureka.co to know more"}
    courses.append(course)
    return jsonify({'Created': course})


@app.route("/courses/<int:course_id", methods=['PUT'])
def update_course(course_id):
    courses[course_id]['Description'] = "XYZ"
    return jsonify({'course': courses[course_id]})


if __name__ == "__main__":
    app.run(debug=True)
