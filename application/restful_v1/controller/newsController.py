from application.base.redPrint import RedPrint
from application.restful_v1.libs.token_auth import auth
from application.restful_v1.service import newsService
from application.restful_v1.validators.newsForms import NewsForm, GetNewsForm

api=RedPrint('news')

@api.route('/test',methods=['GET'])
@auth.login_required
def test():
    return 'test'



@api.route('/saveNews', methods=['POST'])
def save_News():
    """
    保存新闻
    :return:
    """
    form = NewsForm()
    if form.validate_for_api():
        result=newsService.saveNews(form)
        return result

@api.route('/getNews', methods=['GET'])
def get_News():
    """
    获取新闻
    :return:
    """
    form = GetNewsForm()
    if form.validate_for_api():
        result = newsService.getNews(form)
        return result

