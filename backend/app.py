from flask import Flask, Blueprint
from flask_migrate import Migrate
from config import Config
from models import db
from routes.student_routes import student_blueprint
from routes.class_routes import class_blueprint
from routes.subject_routes import subject_blueprint
from routes.enrollment_routes import enrollment_blueprint

# Khởi tạo ứng dụng Flask
app = Flask(__name__)
app.config.from_object(Config)

# Khởi tạo cơ sở dữ liệu và migration
db.init_app(app)
migrate = Migrate(app, db)

# Đăng ký blueprint cho route
api_blueprint = Blueprint('api', __name__, url_prefix='/api')

# Đăng ký các Blueprint con vào api_blueprint
app.register_blueprint(student_blueprint, url_prefix='/api/students')
app.register_blueprint(class_blueprint, url_prefix='/api/classes')
app.register_blueprint(subject_blueprint, url_prefix='/api/subjects')
app.register_blueprint(enrollment_blueprint, url_prefix='/api/enrollments')

if __name__ == '__main__':
    app.run(debug=True)
