from flask import current_app

app=current_app

@app.route('/index',methods=['GET'])
def app_test():
    return 'hello world'
