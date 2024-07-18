import json
from collections import Counter

def convert_to_seconds(tm):
    if len(tm) > 5:
        return int(sum([float(a)*float(b) for a,b in zip(tm.split(':'),[3600,60,1])]))
    else:
        return int(sum([float(a)*float(b) for a,b in zip(tm.split(':'),[60,1])]))


def getdata(id):
    with open(f'{id}.pkr','r',encoding='utf-8') as f:
        data = json.loads(f.read())
        d = data[1] # [1] = the runs, [0] = countries
        event_count = len(set([x['Event'] for x in d['runs']]))
        title = d['title']
#        return data[1]['runs'], data[1]['title'], event_count

    c = Counter([x['Event'] for x in d])

    c[f'Events: {event_count}'] =  10

    for yr in [x['Run Date'][-4:] for x in data]:
        c[yr]=9

    runner_id = f"A{id}"
    runner_name = f"{title[:title.index(' ')]}"
    runner_num_runs = f'Runs:{len(data)}'
    
    c[runner_name]     = min(11, len(d))
    c[runner_id]       = min(12, len(d))
    c[runner_num_runs] = min(12, len(d))

    pbsecs = min([convert_to_seconds(x['Time']) for x in d])
    pb = 'PB: ' + str(datetime.timedelta(seconds=pbsecs))[-5:]
    c[pb] = min(12, len(data))

    return c    
