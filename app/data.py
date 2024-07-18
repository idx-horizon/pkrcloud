import json

def getdata(id):
    with open(f'{id}.pkr','r',encoding='utf-8') as f:
        data = json.loads(f.read())
        event_count = len(set([x['Event'] for x in data[1]['runs']]))
        return data[1]['runs'], data[1]['title'], event_count

    c = Counter([x['Event'] for x in data])

    c[f'Events: {event_count}'] =  10

#    yrc = Counter()
#    yrc.update([x['Run Date'][-4:] for x in data])

    for yr in [x['Run Date'][-4:] for x in data]:
        c[yr]=9

    runner_id = f"A{id}"
    runner_name = f"{title[:title.index(' ')]}"
    runner_num_runs = f'Runs:{len(data)}'
    
    c[runner_name]     = min(11, len(data))
    c[runner_id]       = min(12, len(data))
    c[runner_num_runs] = min(12, len(data))

    pbsecs = min([convert_to_seconds(x['Time']) for x in data])
    pb = 'PB: ' + str(datetime.timedelta(seconds=pbsecs))[-5:]
    c[pb] = min(12, len(data))

    return c    
