from application import app
from flask_script import Manager


if __name__ == '__main__':
    # manager=Manager(app)
    # manager.run()
    app.run(host='127.0.0.1', port=5001)

