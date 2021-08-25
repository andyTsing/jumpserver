import json

from alibabacloud_dysmsapi20170525.client import Client as Dysmsapi20170525Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dysmsapi20170525 import models as dysmsapi_20170525_models


class AlibabaSMS:
    def __init__(self, access_key_id: str, access_key_secret: str):
        config = open_api_models.Config(
            # 您的AccessKey ID,
            access_key_id=access_key_id,
            # 您的AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = 'dysmsapi.aliyuncs.com'
        self.client = Dysmsapi20170525Client(config)

    def send_sms(self, phone_numbers: list, sign_name: str, template_code: str, template_param: dict):
        phone_numbers_str = ','.join(phone_numbers)
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
            phone_numbers=phone_numbers_str, sign_name=sign_name,
            template_code=template_code, template_param=json.dumps(template_param)
        )
        # 复制代码运行请自行打印 API 的返回值
        response = self.client.send_sms(send_sms_request)
        return response
