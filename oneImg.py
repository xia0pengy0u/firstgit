# coding:utf-8
import base64
from urllib import request, parse
import os, json


# 读取文件夹中所有的图片
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files  # 当前路径下所有非目录子文件


# filesname = file_name(r'C:\Users\13689\Desktop\应用系统-JPG 2')
# filesname = [r'C:\Users\13689\Desktop\bb.jpg']

access_token = "24.b5aaec7b59e1a45e4950d1fbdab8c11d.2592000.1567212913.282335-16927906"
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=' + access_token
# 二进制方式打开图文件

b = open('./orc.doc', 'a', encoding='utf8')

f = open('./4.jpg', 'rb')

# 参数image：图像base64编码
img = base64.b64encode(f.read())
f.close()
params = {"image": img}
params = parse.urlencode(params)
requests = request.Request(url, params.encode('utf-8'))
requests.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = request.urlopen(requests)
content = response.read().decode('utf-8')
contents = json.loads(content, encoding='utf-8')
print(contents)
if contents:
    resulelist = contents["words_result"]
    for word in resulelist:
        result = word['words'] + '\n'
        b.write(result)
    b.write('\r\n\n\n')

