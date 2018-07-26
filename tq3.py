import urllib.parse
import urllib.request
import json
import xml.etree.ElementTree as ET


tree = ET.parse('city.xml')
root = tree.getroot()
city_area = input('请输入查询区域:')
for each in root:
    if city_area in each.attrib.values():
        city_id = each.attrib['id']

host = 'http://freecityid.market.alicloudapi.com'
path = '/whapi/json/alicityweather/briefforecast3days'
method = 'POST'
appcode = '708efccf6eb5445fae08702f68c5695c'
querys = ''
bodys = {}
url = host+path
bodys['cityId'] = city_id
bodys['token'] = '677282c2f1b3d718152c4e25ed434bc4'
post_data = urllib.parse.urlencode(bodys).encode('utf-8')
request = urllib.request.Request(url, post_data)
request.add_header('Authorization', 'APPCODE'+' ' + appcode)
request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read().decode()
content = json.loads(content)
print(content['data']['city']['name'])
for i in range(3):
    print(content['data']['forecast'][i]['predictDate'])
    print(content['data']['forecast'][i]['conditionDay'])
    print(content['data']['forecast'][i]['tempDay']+'摄氏度')
    print(content['data']['forecast'][i]['windDirDay'])
    print('***********')
