import datetime

import func
import func_detect
import func_parse

from lxml import etree


# def elements_to_output(obj, config):
#     list_result = []
#     for i in obj:
#         temp = func_parse.parse_config_html({}, config['data'], {}, i)
#         if temp:
#             list_result.append(temp)
#     return list_result


def list_string_to_output(obj, config):
    if config['type_output'] == 2:
        result = func_detect.detect_type_find(obj, config)
        return [i.strip() for i in result if len(i.strip()) > 0]
    elif config['type_output'] == 3:
        list_numb = []
        for i in obj:
            list_numb.append(int(func_detect.detect_type_find(func.remove_space("".join(i)).strip(), config)))
        return list_numb
    elif config['type_output'] == 4:
        new_string = ""
        for _string in obj:
            temp = func_detect.detect_type_find(func.remove_space("".join(_string)).strip(), config)
            if isinstance(temp, list):
                temp = temp[0]
            new_string += temp + " "
        return new_string.strip()
    elif config['type_output'] == 5:
        numb = func_detect.detect_type_find(func.remove_space("".join(obj)).strip(), config)
        return int(numb)
    elif config['type_output'] == 6:
        time_string = func_detect.detect_type_find(obj, config)
        return func_detect.format_time(time_string, config)
    elif config['type_output'] == 8:
        # return html từ list htmlElement
        _html = ""
        for i in obj:
            _html = _html.join(etree.tostring(i, encoding='unicode'))
        return _html


def list_int_to_output(obj, config):
    if config['type_output'] == 3:
        return obj


def string_to_output(obj, config):
    if config['type_output'] == 3:
        obj = func_detect.detect_type_find(func.remove_space("".join(obj).strip()), config)
        return [int(i) for i in obj]
    elif config['type_output'] == 4:
        obj = func_detect.detect_type_find(func.remove_space("".join(obj)).strip(), config)
        return "".join(obj).strip()
    elif config['type_output'] == 5:
        obj = func_detect.detect_type_find(func.remove_space("".join(obj)).strip(), config)
        if isinstance(obj, list):
            return int(obj[0])
        else:
            return int(obj)
    elif config['type_output'] == 2:
        pass
    elif config['type_output'] == 6:
        obj = func_detect.detect_type_find(func.remove_space("".join(obj)).strip(), config)
        time = func_detect.detect_time_format(obj, config)
    elif config['type_output'] == 7:
        obj = func.remove_space("".join(obj))
        if obj == config['true']:
            return True
        elif obj == config['false']:
            return False


def int_to_output(obj, config):
    if config['type_output'] == 5:
        return obj
    elif config['type_output'] == 2:
        pass
    elif config['type_output'] == 3:
        pass
    elif config['type_output'] == 4:
        pass
    elif config['type_output'] == 6:
        pass


def datetime_to_output(obj, config):
    pass


def timestamp_to_output(obj, config):
    if config['type_output'] == 6:
        obj = func_detect.detect_type_find(obj, config)[0]
        obj = datetime.datetime.fromtimestamp(int(obj)/1000)
        return obj
    elif config['type_output'] == 3:
        pass
    elif config['type_output'] == 4:
        pass
    elif config['type_output'] == 5:
        pass
    elif config['type_output'] == 2:
        pass
