import sys
import datetime

import func
import func_parse
import func_action
import func_request_find
import func_input_to_ouput
from config import config_env

from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def detect_type_action(browser, config, match):
    # config truyen vao la config cua doi tuong
    if config['type_action'] == 1:
        func_action.action_click(browser, config)
    elif config['type_action'] == 2:
        list_link = func_action.action_get_attribute(browser, config)
        return list_link
    elif config['type_action'] == 3:
        return func_action.action_scroll_down()
    elif config['type_action'] == 4:
        func_action.action_send_keys(browser, config, match)
    elif config['type_action'] == 5:
        return func_parse.parse_config_browser({}, config['data'], {}, browser)
    elif config['type_action'] == 6:
        return func_action.action_enter(browser, config)


def detect_type_response(response, config):
    if config['type_response'] == 0:
        return config
    elif config['type_response'] == 1:
        response = html.fromstring(response.text, 'lxml')
        return response
    elif config['type_response'] == 2:
        response = response.json()
        return response


def detect_type_crawl(config):
    if config['type_crawl'] == 1:
        return func_request_find.send_request_get(config['url'])
    elif config['type_crawl'] == 2:
        return func_request_find.selenium_send_request(config['url'])


def detect_type_result(result, config):
    try:
        type_result = config['type_result'] 
        if type_result == 1:
            # bóc tách list htmlElement
            list_result = []
            dict_result = {}
            for i, val in enumerate(result):
                temp = func_parse.parse_config_html({}, config['data'], {}, val)
                try:
                    if config['auto_increment'] == True:
                        if temp:
                            dict_result[config['key'] + str(i + 1)] = temp
                    
                except:
                    if temp:
                        list_result.append(temp)
            if list_result:
                return list_result
            else:
                return dict_result
        elif type_result == 2:
            return func_input_to_ouput.list_string_to_output(result, config)
        elif type_result == 3:
            return func_input_to_ouput.list_int_to_output(result, config)
        elif type_result == 4:
            return func_input_to_ouput.string_to_output(result, config)
        elif type_result == 5:
            return func_input_to_ouput.int_to_output(result, config)
        elif type_result == 6:
            return func_input_to_ouput.datetime_to_output(result, config)
        elif type_result == 7:
            return func_input_to_ouput.timestamp_to_output(result, config)
        elif type_result == 8:
            # result là list htmlElement, sinh thêm key cho data
            list_result = []
            for i in result:
                temp = func_parse.parse_config_html({}, config['data'], {}, i)
                if temp:
                    list_result.append(temp)
    except:
        return None


def detect_type_find(obj, config):
    if config['type_find'] == 1: # giữ nguyên obj
        return obj
    elif config['type_find'] == 2: # tìm theo regex
        return func.regex_extract(obj, config)
    elif config['type_find'] == 3: # split
        new_time_list = []
        time_list = []
        for i in obj:
            result = func.regex_split(i, config)
            time_list.extend(result)
        for i in config['position_split']:
            new_time_list.append(time_list[i].strip())
        return "".join(new_time_list)


def detect_type_replace(obj, config):
    if config['type'] == 2:
        if config['old_val'] == "year":
            obj = obj.replace(year=config['new_val'])
        elif config['old_val'] == "month":
            obj = obj.replace(month=config['new_val'])
        elif config['old_val'] == "day":
            obj = obj.replace(day=config['new_val'])
    return obj

def format_time(time, config):
    if type(time) == list:
        time = "".join(time)
    # print(time)
    time_format = config['time_format'].replace("days","%d").replace("months","%m").replace("years","%Y").replace("hours","%H").replace("minutes","%M").replace("seconds","%S").replace("microseconds", "%f")
    time = datetime.datetime.strptime(time, time_format)

    try:
        for conf_replace in config['replace']:
            time = detect_type_replace(time, conf_replace)
    except:
        pass
    time = time + datetime.timedelta(microseconds=100000)
    return time


def detect_browser_result(browser, config):
    if config['browser_result'] == 1:
        try:
            result = func_request_find.browser_find_xpath(browser, config['xpath'])
        except:
            return None
        if config['attribute'] == 'text':
            result = result.text
        else:
            result = result.get_attribute(config['attribute'])
        result = detect_type_result(result, config)
        return result
    elif config['browser_result'] == 2:
        try:
            results = func_request_find.browser_finds_xpath(browser, config['xpath'])
        except:
            return None
        list_result = []
        if config['attribute'] == 'text':
            for i in results:
                list_result.append(i.text)
        else:
            for i in result:
                list_result.append(i.get_attribute(config['attribute']))
        result = detect_type_result(list_result, config)     
        return result
    elif config['browser_result'] == 3:
        try:
            results = func_request_find.browser_finds_xpath(browser, config['xpath'])
        except:
            return None
        
        # try:
        #     list_result = {}
        #     if config['auto_increment'] is True:
        #         for i, v in enumerate(result):
        #             temp = func_parse.parse_config_browser({}, config['data'], {}, i)
        #             if temp:
        #                 list_result.update()
        # except:
        list_result = []
        for i in results:
            temp = func_parse.parse_config_browser({}, config['data'], {}, i)
            if temp:
                list_result.append(temp)
        try:
            if config['auto_increment'] is True:
                list_auto_increment = {}
                list_result.reverse()
                for i, luot_da in enumerate(list_result):
                    list_obj = []
                    for key, val in luot_da.items():
                        list_obj.extend(val)
                    list_auto_increment[config['key'] + str(i + 1)] = list_obj
            return list_auto_increment
        except:        
            return list_result
