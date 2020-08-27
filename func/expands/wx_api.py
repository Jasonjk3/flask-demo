from requests import post, get
import json
class WX_API():
    """
    微信消息模板调用api
    """
    def __init__(self,appId='',secret=''):
        self.appId=appId
        self.secret=secret

    def get_token(self):

        wx_token_api = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s"%(self.appId,self.secret)
        response=get(wx_token_api).json()
        try:
            token=response['access_token']
            return token
        except Exception as e:
            print("获取token失败,",e)
    def send_msg(self,openId,tempId,data,token,url=''):
        wx_api = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s" % token
        wx_parm = {"touser": openId,
                   "template_id": tempId,
                   "data": data,
                   "url":url}
        wx_json = json.dumps(wx_parm)
        # print(wx_json)
        try:
            resp = post(wx_api, wx_json)
            msg = resp.json()
            return msg
        except Exception as e:
            return e



if __name__ == '__main__':
    token=WX_API().get_token()
    data = {
        "first": {
            "value": "恭喜你购买成功！",
            "color": "#173177"
        },
        "keyword1": {
            "value": "巧克力\n 123123213123213",
            "color": "#173177"
        },
        "keyword2": {
            "value": "39.8元",
            "color": "#173177"
        },
        "keyword3": {
            "value": "2014年9月22日",
            "color": "#173177"
        },
        "remark": {
            "value": "欢迎再次购买！",
            "color": "#173177"
        }
    }
    url='http://www.long58.com.cn/sop'
    rep=WX_API().send_msg(openId="o5N0quHwv2dPYcCJnnde7_bDRxXM",tempId="NRcy1S73-isr5GTr0dpRoZ481SHrZ0NuxcsHhPJfCTA",data=data,token=token,url=url)
    print(rep)