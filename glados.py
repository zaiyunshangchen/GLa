import requests,json,os
# -------------------------------------------------------------------------------------------
# github workflows
# -------------------------------------------------------------------------------------------


if __name__ == '__main__':
# pushplus秘钥 申请地址 http://www.pushplus.plus
    sckey = os.environ.get("PUSHPLUS_TOKEN", "")
# 推送内容
    sendContent = ''
# glados账号cookie 直接使用数组 如果使用环境变量需要字符串分割一下
    cookies = os.environ.get("GLADOS_COOKIE", []).split("&")
    if cookies[0] == "":
        print('未获取到COOKIE变量') 
        cookies = []
        exit(0)
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    origin = "https://glados.rocks"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    payload={
        'token': 'glados.one'
    }
    for cookie in cookies:
        checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent,'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
        state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent})
    #--------------------------------------------------------------------------------------------------------#  
        #time = state.json()['data']['leftDays']
        #echo(time)
        time = str(state.json()['data']['leftDays']).split('.')[0]
        #time = time.split('.')[0]
        email = state.json()['data']['email']
        if 'message' in checkin.text:
            mess = checkin.json()['message']
            print(email+'----结果--'+mess+'----剩余('+time+')天')  # 日志输出
            sendContent += email+'----'+mess+'----剩余('+time+')天\n'
        else:
            requests.get('http://www.pushplus.plus/send?token=' + sckey + '&content='+email+'cookie已失效')
            print('cookie已失效')  # 日志输出
     #--------------------------------------------------------------------------------------------------------#   
    if sckey != "":
         requests.get('http://www.pushplus.plus/send?token=' + sckey + '&title='+email+'签到成功'+'&content='+sendContent)

import requests
import random


def get_headers(header_raw):
    return dict(line.split(": ", 1) for line in header_raw.split("\n") if line != '')


headers_str = '''
accept: application/json, text/javascript, */*; q=0.01
accept-language: zh-CN,zh;q=0.9
content-type: application/x-www-form-urlencoded;charset=UTF-8
Accept-Encoding: gzip, deflate
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36
'''
headers = get_headers(headers_str)

message_dict = {'dlc@163.com': 'chenazx123'}

for key, value in message_dict.items():
    step = random.randint(10000, 20000)
    data = {
        "referrer": "http://bs.yanwan.store/",
        "referrerPolicy": "strict-origin-when-cross-origin",
        "method": "POST",
        "mode": "cors",
        "credentials": "omit",
        "user": "%s" % key,
        "password": "%s" % value,
        "step": "%s" % step,
        "ver": "cxydzsv3.2"
    }
    response = requests.post(url="http://yanwan.store/run4/mi.php", headers=headers, data=data)



 




