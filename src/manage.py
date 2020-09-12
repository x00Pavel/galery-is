from flask_script import Manager, commands
from src.festival_is import app

manager = Manager(app)


@manager.command
def init_db():
    with app.test_request_context():
        from src.festival_is_db.create_db import db

        db.engine.echo = True
        db.metadata.bind = db.engine
        db.metadata.create_all(checkfirst=True)


if __name__ == "__main__":
    manager.run()