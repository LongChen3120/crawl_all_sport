import sys
import json
import copy
import time
import logging
import datetime

import pymongo

from config import config_env


log_main = logging.getLogger(config_env.NAME_LOG_1)
log_ram = logging.getLogger(config_env.NAME_LOG_2)


# import main
import func
from config import config_env

from elasticsearch import Elasticsearch

            
def connect_DB_local():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db_wc = client["PaPer"]
    return db_wc


def connect_DB_aHuy():
    client = pymongo.MongoClient("mongodb://192.168.19.168:27017")
    db_paper = client['PaPer']
    return db_paper


def connect_col_config_crawl_sport():
    db_paper = connect_DB_local()
    return db_paper['config_crawl_sport']


def connect_col_log():
    db_paper = connect_DB_local()
    return db_paper['log']


def connect_col_lich_sport():
    db_paper = connect_DB_local()
    return db_paper['lich_sports']


# def read_config_lich():
#     col_config = connect_col_config()
#     return col_config.


def check_config(topic):
    # hàm tìm kiếm config dựa vào url
    # nhận vào url chứa domain của website
    # trả về config của website đó
    with open(config_env.PATH_CONFIG_DETAIL, 'r', encoding='utf-8') as rf:
        list_config = json.load(rf)
    
    for config in list_config:
        if config['topic'] == topic:
            return config


def up_log():
    # hàm up log lên db
    col_log = connect_col_log()
    with open(config_env.PATH_LOG_1, 'r', encoding='utf-8') as read_log_main:
        list_log_main = []
        for line in read_log_main:
            line = line.split(' - ')
            list_log_main.append({
                "type_log":config_env.TYPE_LOG_1,
                "time":line[0],
                "lever":line[1],
                "message":line[2]
            })
        insert_DB(col_log, list_log_main)
    with open('./doc/log_ram/ram.log', 'r', encoding='utf-8') as read_log_ram:
        list_log_ram = []
        for line in read_log_ram:
            line = line.split(' - ')
            list_log_ram.append({
                "type_log":config_env.TYPE_LOG_2,
                "time":line[0],
                "lever":line[1],
                "message":line[2]
            })
        insert_DB(col_log, list_log_ram)


def insert_DB(col, list_data):
    col.insert_many(list_data)


def update_lich_DB(col, list_data):
    for match in list_data:
        filter = {"team_0":match['team_0'], "team_1":match['team_1'],"time":match['time'], "domain":match['domain']}
        if col.find_one(filter):
            vals = {"$set":match}
            col.update_one(filter, vals)
        else:
            col.insert_one(match)


def update_bxh_DB(col, list_data):
    for team in list_data:
        filter = {"group":team['group'], "team":team['team'], "domain":team['domain']}
        if col.find_one(filter):
            vals = {"$set":team}
            col.update_one(filter, vals)
        else:
            col.insert_one(team)


def update_config():
    col_config_crawl_sport = connect_col_config_crawl_sport()
    with open(config_env.PATH_CONFIG, 'r', encoding='utf-8') as read_config:
        data_config = json.load(read_config)
    for config in data_config:
        try:
            if col_config_crawl_sport.find_one({"league":config['league'], "sport_name":config['sport_name'], "url":config['url']}):
                mapping_site = {"league":{"$regex":f"{config['league']}"}, "sport_name":{"$regex":f"{config['sport_name']}"}, "url":config['url']}
                update_vals = {"$set":config}
                col_config_crawl_sport.update_one(mapping_site, update_vals)
            else:
                col_config_crawl_sport.insert_one(config)
        except:
            print(config)


def connect_ES():
    es = Elasticsearch(hosts=config_env.HOST_ES)
    return es


def create_index():
    local_es = Elasticsearch(hosts=config_env.HOST_ES)
    try:
        local_es.indices.create(index=config_env.INDEX_ES)
    except:
        pass
# create_index()


def find_next_match(es, index_es):
    # search trận đấu có time > time hiện tại
    query_search = {
        "size": 1, 
        "sort": [
            {
                "time": {
                    "order": "asc"
                }
            }
        ],
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "type": 2
                        }
                    },
                    {
                        "range": {
                            "time":{
                                "gt": datetime.datetime.now()
                            }
                        }
                    }
                ]
            }
        }
    }
    match = es.search(index=index_es, body=query_search)
    return match['hits']['hits'][0]


def find_by_id(es, index_es, id):
    # tìm kiếm trận đấu theo id
    query_search = {
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "_id": id
                        }
                    }
                ]
            }
        }
    }
    match = es.search(index=index_es, body=query_search)
    return match['hits']['hits'][0]


def update_by_id(es, index_es, id_match, data):
    # update trận đấu theo id
    query_update = {
        "doc":data
    }
    try:
        es.update(index=index_es, id=id_match, body=query_update)
    except Exception as e:
        print(e)
    

def search_doc(es, index_es, query):
    return es.search(index = index_es, body = query)


def insert_ES(es, es_index, list_data):
    for match in list_data:
        es.index(index=es_index, body=match)


def update_lich_ES(es, es_index, list_data):    
    check_update = False
    for match in list_data:
        query = {
            "query": {
                "bool": {
                    "must":[
                        {
                            "match":{
                                "type":match['type']
                            }
                        },
                        {
                            "match":{
                                "team_0":{
                                    "query":match['team_0'],
                                    "operator" : "AND"
                                }
                            }
                        },
                        {
                            "match":{
                                "team_1":{
                                    "query":match['team_1'],
                                    "operator" : "AND"
                                }
                            }
                        },
                        {
                            "match":{
                                "time":match['time']
                            }
                        },
                        {
                            "match":{
                                "domain":{
                                    "query":match['domain'],
                                    "operator": "AND"
                                }
                            }
                        }
                    ]
                }
            }            
        }
        result =  es.search(index=es_index, body=query)
        if result['hits']['total']['value'] >= 1:
            del match['create_date']
            id_match = result['hits']['hits'][0]['_id']
            query_update = {
                "doc":match
            }
            response = es.update(index=es_index, id=id_match, body=query_update)
            if response['result'] == "updated":
                # logging.warning(f"update lich ok, id:{id_match}")
                check_update = True
        else:
            # logging.warning(f"insert match id:{id_match}")
            check_update = True
            es.index(index=es_index, body=match)
    return check_update


def update_bxh_ES(es, es_index, list_data):
    check_update = False
    for team in list_data:
        query_find = {
            "query": {
                "bool": {
                    "must":[
                        {
                            "match":{
                                "group":{
                                    "query":team['group'],
                                    "operator" : "AND"
                                }
                            }
                        },
                        {
                            "match":{
                                "team":{
                                    "query":team['team'],
                                    "operator" : "AND"
                                }
                            }
                        },
                        {
                            "match":{
                                "domain":{
                                    "query":team['domain'],
                                    "operator" : "AND"
                                }
                            }
                        }
                    ]
                }
            }            
        }
        result =  es.search(index=es_index, body=query_find)
        if result['hits']['total']['value'] >= 1:
            del team['create_date']
            id_team = result['hits']['hits'][0]['_id']
            query_update = {
                "doc":team
            }
            response = es.update(index=es_index, id=id_team, body=query_update)
            if response['result'] == "updated":
                check_update = True
        else:
            es.index(index=es_index, body=team)
            check_update = True
    return check_update


def update_sport_es(es, es_index, list_data):
    query_find = {
        "size":1,
        "query": {
            "bool": {
                "must":[
                ]
            }
        }            
    }
    # count_update = 0
    # count_insert = 0
    for data in list_data:
        temp_query = copy.deepcopy(query_find)
        try:
            if data['type']:
                temp_query['query']['bool']['must'].append(
                    {
                        "match":{
                            "type":{
                                "query":data['type'],
                                "operator" : "AND"
                            }
                        }
                    }
                )
        except:
            pass
        try:
            if data['url']:
                temp_query['query']['bool']['must'].append(
                    {
                        "match":{
                            "url":{
                                "query":data['url'],
                                "operator" : "AND"
                            }
                        }
                    }
                )
        except:
            pass
        try:
            if data['league']:
                temp_query['query']['bool']['must'].append(
                    {
                        "match":{
                            "league":{
                                "query":data['league'],
                                "operator" : "AND"
                            }
                        }
                    }
                )
        except:
            pass
        try:
            if data['events']:
                temp_query['query']['bool']['must'].append(
                    {
                        "match":{
                            "events":{
                                "query":data['events'],
                                "operator" : "AND"
                            }
                        }
                    }
                )
        except:
            pass
        try:
            if data['time_start']:
                temp_query['query']['bool']['must'].append(
                    {
                        "match":{
                            "time_start":{
                                "query":data['time_start'],
                                "operator" : "AND"
                            }
                        }
                    }
                )
        except:
            pass
        try:
            if data['time_end']:
                temp_query['query']['bool']['must'].append(
                    {
                        "match":{
                            "time_end":{
                                "query":data['time_end'],
                                "operator" : "AND"
                            }
                        }
                    }
                )
        except:
            pass
        try:
            if data['list_team']['detail_team_0']['name']:
                temp_query['query']['bool']['must'].append(
                    {
                        "match":{
                            "list_team.detail_team_0.name":{
                                "query":data['list_team']['detail_team_0']['name'],
                                "operator" : "AND"
                            }
                        }
                    }
                )
        except:
            pass
        try:
            if data['list_team']['detail_team_1']['name']:
                temp_query['query']['bool']['must'].append(
                    {
                        "match":{
                            "list_team.detail_team_1.name":{
                                "query":data['list_team']['detail_team_1']['name'],
                                "operator" : "AND"
                            }
                        }
                    }
                )
        except:
            pass
        try:
            if data['team']:
                temp_query['query']['bool']['must'].append(
                    {
                        "match":{
                            "team":{
                                "query":data['team'],
                                "operator" : "AND"
                            }
                        }
                    }
                )
        except:
            pass
        try:
            if data['title']:
                temp_query['query']['bool']['must'].append(
                    {
                        "match":{
                            "title":{
                                "query":data['title'],
                                "operator" : "AND"
                            }
                        }
                    }
                )
        except:
            pass
        
        result_search =  es.search(index=es_index, body=temp_query)
        if result_search['hits']['total']['value'] >= 1:
            try:
                del data['create_date']
            except:
                print(data)
            id_team = result_search['hits']['hits'][0]['_id']
            query_update = {
                "doc":data
            }
            result_update = es.update(index=es_index, id=id_team, body=query_update)
            # if result_update['result'] == "updated":
                # count_update += 1
        else:
            es.index(index=es_index, body=data)
            # count_insert += 1
    # log_main.info(f"count update:{count_update}")
    # log_main.info(f"count insert:{count_insert}")
