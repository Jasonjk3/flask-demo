
from application.base import log, ajaxResponse
from application.base.httpException import ServerError
from application.restful_v1.model.news import News
from application.restful_v1.model.user import User


def saveNews(form):
    """
    保存新闻
    :param form:
    :return:
    """
    try:
        log.info("成功 - Parameter:{}".format(form))
        news = News()
        news.author=form.author.data
        news.title=form.title.data
        news.content = form.content.data
        news.date = form.date.data
        result=news.save()
        print(result)
        return ajaxResponse.success(message="保存成功")
    except Exception as e:
        log.error("错误 - {}".format(e))
        raise ServerError()

def getNews(form):
    """
    获取新闻
    :param form:
    :return:
    """
    try:
        log.info("成功 - Parameter:{}".format(form))
        users = User.objects.with_id(form.id.data).skip((1-form.page)*form.limit.data).\
            limit(form.limit.data)
        if users:
            datas=[]
            for i in users:
                datas.append(i.to_mongo())
            return ajaxResponse.success(data=datas, message="获取新闻成功")
        else:
            return ajaxResponse.fail(message="无此新闻")
    except Exception as e:
        log.error("错误 - {}".format(e))
        raise ServerError()