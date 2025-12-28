import os
import requests
from lxml import etree
import json
from datetime import datetime

PROXIES = 'http://127.0.0.1:7890'
URL = 'https://steamcommunity.com/profiles/76561199167491270/friends/'

os.environ['HTTP_PROXY'] = PROXIES
os.environ['HTTPS_PROXY'] = PROXIES

def get_data():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url=URL, headers= headers, timeout=10).text
    doc = etree.HTML(response)
    friends = doc.xpath('//*[starts-with(@id, "fr_")]')
    flist = []
    for i in friends:
        steamid = i.get('data-steamid')
        href_list = i.xpath('.//a[contains(@class,"selectable_overlay")]/@href')
        href = href_list[0] if href_list else None
        img_list = i.xpath('.//img[1]/@src')
        img_url = img_list[0] if img_list else None
        name = i.xpath('normalize-space(.//div[contains(@class,"friend_block_content")]/text()[1])')
        item = {
            'steamid': steamid,
            'href': href,
            'img': img_url,
            'name': name
        }
        flist.append(item)
    return flist
    
def save_json(flist):
    dir = os.path.abspath(__file__)
    base_dir = os.path.dirname(dir)
    json_path = os.path.join(base_dir, 'JSON')
    if not os.path.exists(json_path):
        os.makedirs(json_path)
    today = datetime.now().strftime('%Y%m%d%H%M%S')
    count = len(flist)
    file_name = f'{today}-{count}.json'
    file_path = os.path.join(json_path, file_name)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(flist, f, ensure_ascii=False, indent=2)
    return file_path

if __name__ == "__main__":
    a = save_json(get_data())
    print('===============保存完成===============')
    print(a)
    print('======================================')
    input("press any key to close ......")