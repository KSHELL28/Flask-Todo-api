from flask import Flask

from app.routes.get_tasks import task_bp
from app.routes.create_task import add_bp
from app.routes.delete_task import delete_bp
from app.routes.update_status import update_bp

def create_app(test_config = None):
    app = Flask(__name__)

    app.config["DATABASE"] = "app/database/Todo.db"

    if test_config is not None :
        app.config.update(test_config)
        
    app.register_blueprint(task_bp)
    app.register_blueprint(add_bp)
    app.register_blueprint(delete_bp)
    app.register_blueprint(update_bp)

    return app