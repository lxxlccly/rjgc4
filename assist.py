'''将json文件内容转换为简体字'''
import json
import langconv

address = './poet/tangshisanbaishou.json'
all_poet = []
with open(address, 'r', encoding='utf-8') as load_f:
    load_dict = json.load(load_f)
    for i in range(len(load_dict['content'])):
        all_poet = all_poet + load_dict['content'][i]['content']
for i in range(len(all_poet)):
    all_poet[i]['chapter'] = langconv.Converter('zh-hans').convert(all_poet[i]['chapter'])
    all_poet[i]['author'] = langconv.Converter('zh-hans').convert(all_poet[i]['author'])
    for j in range(len(all_poet[i]['paragraphs'])):
        all_poet[i]['paragraphs'][j] = langconv.Converter('zh-hans').convert(all_poet[i]['paragraphs'][j])
poets = json.dumps(all_poet, ensure_ascii=False, indent=4)
with open('./poet/tssbs.json', 'w', encoding='utf-8') as f:
    f.write(poets)
