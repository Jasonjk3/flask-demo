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



