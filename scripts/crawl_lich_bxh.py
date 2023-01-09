import re
import sys
import json
import logging
import datetime

import requests

import db_handler
import func
import utils
import func_parse
import func_action
import func_detect
import func_request_find
import func_input_to_ouput
from config import config_env

from lxml import html
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


log_main = logging.getLogger(config_env.NAME_LOG_1)
log_ram = logging.getLogger(config_env.NAME_LOG_2)


def format_data_lich_thi_dau(config, list_data):
    list_result = []
    data_sample = config_env.data_lich()
    data_sample['type'] = config['type']
    data_sample['type_detail'] = config['type_detail']
    data_sample['league'] = config['league']
    data_sample['domain'] = config['domain']
    data_sample['url'] = config['url']
    data_sample['create_date'] = datetime.datetime.now()
    for data in list_data:
        temp = data_sample.copy()
        try:
            temp['time_start'] = data['time_start']
            if not temp['time_start']:
                continue
        except:
            continue
        try:
            if data['time_end']:
                temp['time_end'] = data['time_end']
        except:
            pass
        try:
            temp['round'] = data['round']
        except:
            pass

        try:
            temp['group'] = data['group']
        except:
            pass

        try:
            temp['venue'] = data['venue']
        except:
            pass

        try:
            temp['status'] = data['status']
        except:
            pass

        try:
            temp['list_team'] = data['list_team']
        except:
            pass

        try:
            temp['events'] = data['events']
        except:
            pass
        try:
                list_keyword = [config['league'], config['sport_name']]
                for key in list_keyword:
                    if not key:
                        list_keyword.remove(key)
                temp['keyword'] = list_keyword
        except:
            pass
        try:
            temp['keyword_unsign'] = [utils.unicode_to_kodauvagach(i) for i in temp['keyword']] 
        except:
            pass
        try:
            temp['tags'] = data['tags']
        except:
            pass
        list_result.append(temp)
    return list_result


def format_data_ket_qua_thi_dau(config, list_data):
    list_result = []
    data_sample = config_env.data_ket_qua()
    data_sample['type'] = config['type']
    data_sample['type_detail'] = config['type_detail']
    data_sample['league'] = config['league']
    data_sample['sport_name'] = config['sport_name']
    data_sample['domain'] = config['domain']
    data_sample['url'] = config['url']
    data_sample['create_date'] = datetime.datetime.now()
    for data in list_data:
        temp = data_sample.copy()
        try:
            temp['time_start'] = data['time_start']
            temp['time_start'] = data['time_start']
            if not temp['time_start']:
                continue
        except:
            continue
        try:
            temp['time_end'] = data['time_end']
        except:
            pass
        try:
            temp['round'] = data['round']
        except:
            pass

        try:
            temp['group'] = data['group']
        except:
            pass

        try:
            temp['venue'] = data['venue']
        except:
            pass

        try:
            temp['status'] = data['status']
        except:
            pass

        try:
            temp['list_team'] = data['list_team']
        except:
            pass

        try:
            temp['events'] = data['events']
        except:
            pass
        try:
                list_keyword = [config['league'], config['sport_name']]
                for key in list_keyword:
                    if not key:
                        list_keyword.remove(key)
                temp['keyword'] = list_keyword
        except:
            pass
        try:
            temp['keyword_unsign'] = [utils.unicode_to_kodauvagach(i) for i in temp['keyword']] 
        except:
            pass
        try:
            temp['tags'] = data['tags']
        except:
                pass
        list_result.append(temp)
    return list_result


def format_data_bang_xep_hang(config, list_data):
    list_result = []
    if config['type_detail'] == 1:
        for data in list_data:
            data_sample = config_env.type_1_bang_xep_hang()
            data_sample['type'] = config['type']
            data_sample['type_detail'] = config['type_detail']
            data_sample['league'] = config['league']
            data_sample['sport_name'] = config['sport_name']
            data_sample['domain'] = config['domain']
            data_sample['url'] = config['url']
            data_sample['create_date'] = datetime.datetime.now()
            temp = data_sample.copy()
            try:
                temp['team'] = data['team']
            except:
                pass
            try:
                temp['group'] = data['group']
            except:
                pass
            try:
                temp['rank'] = data['rank']
            except:
                pass
            try:
                temp['matches_played'] = data['matches_played']
            except:
                pass
            try:
                temp['wins'] = data['wins']
            except:
                pass
            try:
                temp['draws'] = data['draws']
            except:
                pass
            try:
                temp['losses'] = data['losses']
            except:
                pass
            try:
                temp['win_lose_difference'] = data['win_lose_difference']
            except:
                pass
            try:
                temp['points'] = data['points']
            except:
                pass
            try:
                list_keyword = [config['league'], config['sport_name'], data['team'], data['group']]
                for key in list_keyword:
                    if not key:
                        list_keyword.remove(key)
                temp['keyword'] = list_keyword
            except:
                pass
            try:
               temp['keyword_unsign'] = [utils.unicode_to_kodauvagach(i) for i in temp['keyword']] 
            except:
                pass
            try:
                temp['tags'] = data['tags']
            except:
                pass
            list_result.append(temp)
        return list_result
    elif config['type_detail'] == 3:
        for data in list_data:
            data_sample = config_env.type_3_bang_xep_hang()
            data_sample['type'] = config['type']
            data_sample['type_detail'] = config['type_detail']
            data_sample['league'] = config['league']
            data_sample['sport_name'] = config['sport_name']
            data_sample['domain'] = config['domain']
            data_sample['url'] = config['url']
            data_sample['create_date'] = datetime.datetime.now()
            temp = data_sample.copy()
            try:
                temp['team'] = data['team']
            except:
                pass
            try:
                temp['rank'] = data['rank']
            except:
                pass
            try:
                temp['gold_medal'] = data['gold_medal']
            except:
                pass
            try:
                temp['silver_medal'] = data['silver_medal']
            except:
                pass
            try:
                temp['bronze_medal'] = data['bronze_medal']
            except:
                pass
            try:
                temp['total'] = data['total']
            except:
                pass
            try:
                list_keyword = [config['league'], config['sport_name'], data['team']]
                for key in list_keyword:
                    if not key:
                        list_keyword.remove(key)
                temp['keyword'] = list_keyword
            except:
                pass
            try:
               temp['keyword_unsign'] = [utils.unicode_to_kodauvagach(i) for i in temp['keyword']] 
            except:
                pass
            try:
                temp['tags'] = data['tags']
            except:
                pass
            list_result.append(temp)
        return list_result


def format_data_other_content(config, dict_data):
    data_sample = config_env.data_other_content()
    data_sample['type'] = 8
    data_sample['domain'] = config['domain']
    data_sample['url'] = config['url']
    data_sample['create_date'] = datetime.datetime.now()
    try:
        data_sample['title'] = dict_data['title']
    except:
        pass
    try:
        data_sample['content'] = dict_data['content']
    except:
        pass
    try:
                list_keyword = [dict_data['title']]
                for key in list_keyword:
                    if not key:
                        list_keyword.remove(key)
                data_sample['keyword'] = list_keyword
    except:
        pass
    try:
        data_sample['keyword_unsign'] = [utils.unicode_to_kodauvagach(i) for i in data_sample['keyword']] 
    except:
        pass
    try:
        data_sample['tags'] = dict_data['tags']
    except:
                pass
    return data_sample


def format_data_doi_tuong_thi_dau(config, data):
    if config['other_data']['info']['detail']['type_detail'] == 1:
        pass
    elif config['other_data']['info']['detail']['type_detail'] == 2:
        data_sample = config_env.type_2_doi_tuong_thi_dau()
        data_sample['type'] = config['other_data']['info']['detail']['type']
        data_sample['type_detail'] = config['other_data']['info']['detail']['type_detail']
        data_sample['url'] = config['url']
        data_sample['create_date'] = datetime.datetime.now()
        try:
            data_sample['name'] = data['name']
        except:
            pass
        try:
            data_sample['full_name'] = data['full_name']
        except:
            pass
        try:
            data_sample['IOC_code'] = data['IOC_code']
        except:
            pass
        try:
            data_sample['logo'] = data['logo']
        except:
            pass
        try:
            data_sample['founded'] = data['founded']
        except:
            pass
        try:
            data_sample['numb_of_members'] = data['numb_of_members']
        except:
            pass
        try:
            data_sample['ground'] = data['ground']
        except:
            pass
        try:
            data_sample['capacity'] = data['capacity']
        except:
            pass
        try:
            data_sample['owner'] = data['owner']
        except:
            pass
        try:
            data_sample['manager'] = data['manager']
        except:
            pass
        try:
            data_sample['league'] = data['league']
        except:
            pass
        try:
            data_sample['website'] = data['website']
        except:
            pass
        try:
            list_keyword = [config['league'], config['sport_name'], data['name'], data['full_name']]
            for key in list_keyword:
                if not key:
                    list_keyword.remove(key)
            data_sample['keyword'] = list_keyword
        except:
            pass
        try:
            data_sample['keyword_unsign'] = [utils.unicode_to_kodauvagach(i) for i in data_sample['keyword']] 
        except:
            pass
        try:
            data_sample['tags'] = data['tags']
        except:
            pass

        return data_sample


def crawl_box_detail_wiki(response, config):
    data = {}
    for key, val in config['other_data']['info']['detail']['data'].items():
        if val:
            result = func_request_find.html_find_xpath(response, val['xpath'])
            result = func_detect.detect_type_result(result, val)
            if result:
                data[key] = result
        else:
            data[key] = ""
    return data


def crawl_other_content(es, response, config):
    dict_data = {}
    for key, val in config['other_data']['content'].items():
        try:
            result = func_request_find.html_find_xpath(response, val['xpath'])
            data = func_detect.detect_type_result(result, val)
            if data:
                dict_data.update({key:data})
        except:
            pass
    dict_data = format_data_other_content(config, dict_data)
    db_handler.update_sport_es(es, config_env.INDEX_ES, [dict_data])


def crawl_other_info(es, response, config):
    list_data = []
    try:
        if config['other_data']['info']['type_source'] == 1:
            result = func_request_find.html_find_xpath(response, config['other_data']['info']['link_info']['xpath'])
            list_link_info = func_detect.detect_type_result(result, config['other_data']['info']['link_info'])
            list_link_info = func.make_full_link(config['domain'], list_link_info)
        for link_info in list_link_info:
            config['url'] = link_info
            config['other_data']['info']['url'] = link_info
            response = func_detect.detect_type_crawl(config['other_data']['info'])
            response = func_detect.detect_type_response(response, config['other_data']['info'])
            crawl_other_content(es, response, config)
            data = crawl_box_detail_wiki(response, config)
            data = format_data_doi_tuong_thi_dau(config, data)
            list_data.append(data)
        db_handler.update_sport_es(es, config_env.INDEX_ES, list_data)
    except:
        pass


def crawl():
    # hàm crawl lịch, kết quả, bảng biểu các kiểu con đà điểu

    es = db_handler.connect_ES()
    # lấy config
    col_config_crawl_sport = db_handler.connect_col_config_crawl_sport()
    list_config = col_config_crawl_sport.find({})

    # crawl theo từng config
    for config in list_config:
        if config['end_crawl'] == True:
            continue
        log_main.info(f"crawl url: {config['url']}")
        response = func_detect.detect_type_crawl(config)
        response = func_detect.detect_type_response(response, config)

        # crawl data chính
        result = func_request_find.html_find_xpath(response, config['data']['xpath'])
        list_data = func_detect.detect_type_result(result, config['data'])
        print("_", list_data)
        
        # crawl data phụ: gồm content thêm và đối tượng kèm thêm nếu có
        for key in config['other_data']:
            if key == "content":
                crawl_other_content(es, response, config)
            elif key == "info":
                crawl_other_info(es, response, config)

        # format lại data chính để lưu
        if config['type'] == 1:
            list_data = format_data_lich_thi_dau(config, list_data)
        elif config['type'] == 2:
            list_data = format_data_ket_qua_thi_dau(config, list_data)
        elif config['type'] == 4:
            list_data = format_data_bang_xep_hang(config, list_data)
        print(list_data)
        db_handler.update_sport_es(es, config_env.INDEX_ES, list_data)


        

