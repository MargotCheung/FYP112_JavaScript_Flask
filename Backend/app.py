from flask import Flask
from path import Path

from .views.home import home_view
from .views.lesson import lessonpage_view
from .views.learningProgress import learningProgress_view
from .views.profile import profile_view

PROJECT_DIR = Path(__file__).parent.parent
FRONTEND_DIR = PROJECT_DIR / 'backend'
app = Flask(__name__)


@app.route("/")
def home():
    return home_view()

@app.route("/lessonpage/<row_course_name>")
def lesson(row_course_name):
    return lessonpage_view(row_course_name)

user_id="007"
@app.route('/profile')
def profile():
    return profile_view()

@app.route("/learningProgress/<user_id>")
def learningProgress(user_id):
    return learningProgress_view(user_id)

@app.route("/")
def home():
    return home_view()


if __name__ == "__main__":
    app.run(debug=True)