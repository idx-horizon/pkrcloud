import json

def getdata(id):
    with open(f'{id}.pkr','r',encoding='utf-8') as f:
        data = json.loads(f.read())
        event_count = len(set([x['Event'] for x in data[1]['runs']]))
        return data[1]['runs'], data[1]['title'], event_count
