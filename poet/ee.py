import json
'''
for i in range(58):
    address = './poet.song.' + str(int(i * 1000)) + '.json'
    with open(address, 'r', encoding='utf-8') as load_f:
        load_dict = json.load(load_f)
        for j in range(len(load_dict)):
            if load_dict[j]['author'] == '杜甫':
                print(i)
'''
address = './tangshisanbaishou.json'
with open(address, 'r', encoding='utf-8') as load_f:
    load_dict = json.load(load_f)
    for i in range(len(load_dict['content'])):
        print(load_dict['content'][i]['type'])
