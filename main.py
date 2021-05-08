from application import app
from flask import request

@app.route('/', methods=['GET'])
def index():
    print(request.headers)
    return 'hello'


if __name__ == '__main__':
    # manager=Manager(app)
    # manager.run()
    app.run(host=app.config['RUN_IP'], port=app.config['RUN_PORT'])

