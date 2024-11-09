from flask import Flask, Blueprint
from flask_migrate import Migrate
from config import Config
from models import db
from routes.student_routes import student_blueprint
from routes.class_routes import class_blueprint
from routes.subject_routes import subject_blueprint
from routes.enrollment_routes import enrollment_blueprint

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize database and migration
db.init_app(app)
migrate = Migrate(app, db)

# Create API blueprint
api_blueprint = Blueprint('api', __name__, url_prefix='/api')

# Register sub-blueprints with api_blueprint
api_blueprint.register_blueprint(student_blueprint, url_prefix='/students')
api_blueprint.register_blueprint(class_blueprint, url_prefix='/classes')
api_blueprint.register_blueprint(subject_blueprint, url_prefix='/subjects')
api_blueprint.register_blueprint(
    enrollment_blueprint, url_prefix='/enrollments')

# Register api_blueprint with the main app
app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
