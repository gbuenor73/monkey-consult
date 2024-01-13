import json
from datetime import date, datetime


def list_to_json(list):
    return [item.to_json() for item in list]


def date_handler(obj):
    if isinstance(obj, (date, datetime)):
        return obj.strftime('%d-%m-%Y')
    else:
        return obj


def format_response(obj):
    if type(obj) is list:
        json_dump = json.dumps(obj, default=date_handler)
    else:
        json_dump = json.dumps([obj], default=date_handler)
    return {"data": json.loads(json_dump)}
