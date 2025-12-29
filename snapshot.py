import os
import requests
from lxml import etree
import json
from datetime import datetime
import re

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
    
def load_and_save(flist):
    script_dir = os.path.abspath(__file__)
    base_dir = os.path.dirname(script_dir)
    json_path = os.path.join(base_dir, 'JSON')
    if not os.path.exists(json_path):
        os.makedirs(json_path)
    all_files = os.listdir(json_path)
    pattern = re.compile(r'^\d{14}-\d+\.json$')
    match_files = [i for i in all_files if pattern.match(i)]
    match_files.sort(reverse=True)
    if match_files:
        latest_file = os.path.join(json_path, match_files[0])
        with open(latest_file, "r", encoding='utf-8') as f:
            old_data = json.load(f)
    else:
        old_data = None
    today = datetime.now().strftime('%Y%m%d%H%M%S')
    count = len(flist)
    file_name = f'{today}-{count}.json'
    file_path = os.path.join(json_path, file_name)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(flist, f, ensure_ascii=False, indent=2)
    return old_data, flist

def diff_by_steamid(data_pair):
    old, new = data_pair
    if old == None:
        print('============第一次保存完成===============')
        input("press any key to close ......")
    else:
        old_map ={i['steamid']: i for i in old if i.get('steamid')}
        new_map ={i['steamid']: i for i in new if i.get('steamid')}
        old_ids = set(old_map.keys())
        new_ids = set(new_map.keys())
        added_ids = new_ids - old_ids
        removed_ids = old_ids - new_ids
        added = [new_map[i] for i in added_ids]
        removed = [old_map[i] for i in removed_ids]
        print("============保存完成===============")
        print(f'新增好友{len(added)}个')
        for i in added:
            print(i['name'], i['href'], sep='---->')
        print("===================================")
        print(f'失去好友{len(removed)}个')
        for i in removed:
            print(i['name'], i['href'], sep='---->')
        print("===================================")
        input("press any key to close ......")


if __name__ == "__main__":
    diff_by_steamid(load_and_save(get_data()))
