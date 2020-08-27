from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest



class Sms:
    """
    阿里云短信服务
    """
    def __init__(self,phone,data,sms_AccessKeyId,sms_AccessKeySecret,template='',signName=''):
        self.accessKeyId=sms_AccessKeyId
        self.accessSecret=sms_AccessKeySecret
        self.client = AcsClient(self.accessKeyId, self.accessSecret, 'cn-guangxi')
        self.phone=phone
        self.data = data
        self.template = template
        self.signName = signName
    def sms_send(self):
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('dysmsapi.aliyuncs.com')
        request.set_method('POST')
        request.set_protocol_type('https') # https | http
        request.set_version('2017-05-25')
        request.set_action_name('SendSms')

        request.add_query_param('RegionId', "cn-guangxi")
        request.add_query_param('PhoneNumbers', self.phone)
        request.add_query_param('SignName', self.signName)
        request.add_query_param('TemplateCode', self.template)
        request.add_query_param('TemplateParam', self.data)

        response = self.client.do_action_with_exception(request)
        return (str(response, encoding = 'utf-8'))

