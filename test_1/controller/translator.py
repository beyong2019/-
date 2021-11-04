# 百度通用翻译API,不包含词典、tts语音合成等资源，如有相关需求请联系translate_api@baidu.com
# coding=utf-8

import http.client
import hashlib
import urllib
import random
import json


def translator(q):
    # 百度app_id和密钥需要通过注册百度【翻译开放平台】账号后获得
    global result
    app_id = '20211104000990717'  # 填写你的app_id
    secret_key = 'TMWnnqq9wv9klL4Pn_kv'  # 填写你的密钥

    http_client = None
    my_url = '/api/trans/vip/translate'  # 通用翻译API HTTP地址

    from_lang = 'auto'  # 原文语种
    to_lang = 'zh'  # 译文语种
    salt = random.randint(32768, 65536)
    sign = app_id + q + str(salt) + secret_key
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = my_url + '?appid=' + app_id + '&q=' + urllib.parse.quote(q) + '&from=' + from_lang + \
            '&to=' + to_lang + '&salt=' + str(salt) + '&sign=' + sign

    # 建立会话，返回结果
    try:
        http_client = http.client.HTTPConnection('api.fanyi.baidu.com')
        http_client.request('GET', myurl)
        # response是HTTPResponse对象
        response = http_client.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)

        print(result)
    except Exception as e:
        print(e)
    finally:
        if http_client:
            http_client.close()
    return result
