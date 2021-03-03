from application import app


if __name__ == '__main__':
    # manager=Manager(app)
    # manager.run()
    app.run(host=app.config['RUN_IP'], port=app.config['RUN_PORT'])

