# CIDP校园网自动登录脚本

import requests
import time
import sys
import datetime

f = open('con_cidp.log', 'a')
sys.stdout = f
sys.stderr = f

ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S'
theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)

key = {'DDDDD': '',  # 校园网账号
       'upass': '',  # 校园网密码
       '0MKKey': '%C1%AC%BD%D3%CD%F8%C2%E7'}
url = 'http://10.252.251.251/'


def con_cidp():
    r = requests.post(url, data=key)
    return r.text


def test_authweb():
    try:
        requests.get(url,
                     timeout=0.5)
        return 1
    except:
        return 0


def test_baide():
    try:
        response = requests.get('http://baidu.com/',
                                timeout=0.5)
        if "www.baidu.com" in response.text:
            return 1
    except:
        return 0


if test_baide() == 1:
    print(theTime + '\nTest OK!')
    sys.exit()

if test_authweb() == 0:
    print(theTime + '\nNot AuthWeb!')
    sys.exit()

res = con_cidp()

while 1:
    if "登录成功窗" in res:
        print(theTime + '\nOK!')
        sys.exit()
    print(theTime + '\nNO!')
    time.sleep(3)
    res = con_cidp()
