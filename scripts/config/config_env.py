# _________________ ES _________________
# a huy : 192.168.19.168:49154
# local : http://127.0.0.1:9200/
# a hoat: http://192.168.19.77:9200/
# server: http://10.3.11.253:3008

# _________________ MongoDB _________________
# local mongodb://localhost:27017
# a huy mongodb://192.168.19.168:27017

# ______PATH_____
HOST_ES = "http://127.0.0.1:9200/"
INDEX_ES = "sports"
PATH_DB_MONGO = "mongodb://localhost:27017"
PATH_LOG_1 = "./doc/log_main/main.log"
PATH_LOG_2 = "./doc/log_ram/ram.log"
PATH_CHROME_DRIVER = "./chrome_driver/chromedriver.exe"
PATH_CONFIG = "./scripts/extract/config/config.json"
PATH_CONFIG_DETAIL = "./scripts/extract/config/config_detail.json"
API_SCHEDULE_CRAWL = "http://192.168.19.168:5005/schedule_crawl"


# ______VARIABLES_____
IMPLICITLY_WAIT = 5
NAME_LOG_1 = "main"
TYPE_LOG_1 = 1
NAME_LOG_2 = "log_mem"
TYPE_LOG_2 = 2
HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
TIMEOUT = 10
TIME_RUN_SCHEDULE = 1
MAX_JOBS = 5
PAYLOAD_SCHEDULE_CRAWL = {
    "key": "affcup_live",
    "type": 1,
    "start_time": "2022-12-08T16:36:08.187808",
    "interval": 30,
    "auto_controll_interval": "False",
    "site": "https://vtc.vn/",
    "topic": "AFF Cup Live",
    "kwargs": {
        "schedule_data":[
            {
                "schedule_id": "",
                "team_1": "",
                "team_2": ""
            }
        ] 
    }
}


# ______FUNC_____
def data_football_sample():
    data = {
        "type": None,
        "topic": "",
        "url": "",
        "domain": "",
        "create_date": "",
        "time": "",
        "last_update":None,
        "round":"",
        "group": "",
        "venue": "",
        "status":"",
        "detail_team_0": {
            "name": "",
            "ensign": "",
            "coach": "",
            "bàn thắng": None,
            "scorer": [
                {
                    "name": "",
                    "time": "",
                    "type":None
                }
            ],
            "pen":None,
            "shots": None,
            "shot_on_target": None,
            "possession": "",
            "passes": None,
            "pass_accuracy": "",
            "Fouls": None,
            "numb_yellow_cards": None,
            "numb_red_cards": None,
            "offsides": None,
            "corners": None,
            "position": "",
            "đội hình": [
                {
                    "player": "",
                    "numb": None
                }
            ],
            "Substitutes": [
                {
                    "player": "",
                    "numb": None
                }
            ]
        },
        "detail_team_1": {
            "name": "",
            "ensign": "",
            "coach": "",
            "bàn thắng": "",
            "scorer": [
                {
                    "name": "",
                    "time": "",
                    "type":None
                }
            ],
            "pen":None,
            "shots": None,
            "shot_on_target": None,
            "possession": "",
            "passes": None,
            "pass_accuracy": "",
            "Fouls": None,
            "numb_yellow_cards": None,
            "numb_red_cards": None,
            "offsides": None,
            "corners": None,
            "position": "",
            "đội hình": [
                {
                    "player": "",
                    "numb": None
                }
            ],
            "Substitutes": [
                {
                    "player": "",
                    "numb": None
                }
            ]
        },
        "substitution": [
            {
                "time": "",
                "in": [
                    {
                        "name": "",
                        "team": "",
                        "numb": None
                    }
                ],
                "out": [
                    {
                        "name": "",
                        "team": "",
                        "numb": None
                    }
                ]
            }
        ],
        "card": [
            {
                "time": "",
                "type_card": "",
                "player": "",
                "numb": None,
                "team": ""
            }
        ],
        "dien_bien_tran_dau":[
            {
                "time":"",
                "event":""
            }
        ],
        "dien_bien_pen":{

        },
        "keyword": [],
        "keyword_unsign": [],
        "thread": "",
    }
    return data


def data_lich():
    data = {
        "type": None,
        "type_detail":None,
        "league": "",
        "sport_name":"",
        "url": "",
        "domain": "",
        "create_date": "",
        "time_start": None,
        "time_end": None,
        "round":"",
        "group": "",
        "venue": "",
        "status":"",
        "list_team":{
            
        },
        "events":"",
        "keyword":[],
        "keyword_unsign":[],
        "tags":[]
    }
    return data


def data_ket_qua():
    data = {
        "type": None,
        "type_detail":None,
        "league": "",
        "sport_name":"",
        "url": "",
        "domain": "",
        "create_date": "",
        "time_start": None,
        "time_end": None,
        "round":"",
        "group": "",
        "venue": "",
        "status":"",
        "list_team":{
        },
        "events":"",
        "keyword":[],
        "keyword_unsign":[],
        "tags":[]
    }
    return data


def type_3_bang_xep_hang():
    data = {
        "type": None,
        "type_detail":None,
        "league": "",
        "sport_name":"",
        "url": "",
        "domain": "",
        "create_date": "",
        "team":"",
        "rank":"",
        "gold_medal":"",
        "silver_medal":"",
        "bronze_medal":"",
        "total":"",
        "keyword":[],
        "keyword_unsign":[],
        "tags":[]
    }
    return data


def type_1_bang_xep_hang():
    data = {
        "type": None,
        "type_detail":None,
        "league": "",
        "sport_name":"",
        "url": "",
        "domain": "",
        "create_date": "",
        "team":"",
        "group":"",
        "rank":"",
        "matches_played":"",
        "wins":"",
        "draws":"",
        "losses":"",
        "win_lose_difference":"",
        "points":"",
        "keyword":[],
        "keyword_unsign":[],
        "tags":[]
    }
    return data


def data_other_content():
    data = {
        "type": None,
        "url": "",
        "domain": "",
        "create_date": "",
        "title":"",
        "content":"",
        "keyword":[],
        "keyword_unsign":[],
        "tags":[]
    }
    return data


def type_2_doi_tuong_thi_dau():
    data = {
        "type":None,
        "type_detail":None,
        "url":"",
        "create_date":"",
        "name":"",
        "full_name":"",
        "IOC_code":"",
        "logo":"",
        "founded":"",
        "numb_of_members":"",
        "ground":"",
        "capacity":"",
        "owner":"",
        "manager":"",
        "league":"",
        "website":"",
        "keyword":[],
        "keyword_unsign":[],
        "tags":[]
    }
    return data


