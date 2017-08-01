#coding:utf-8
import json
import os
def get_Frends_list():
    k = 0
    file_list=[i for i in os.listdir('./frends/') if i.endswith('json')]
    frends_list=[]
    for f in file_list:
        with open('./frends/{}'.format(f),'r',encoding='utf-8') as w:
            data=w.read()[95:-5]
            js=json.loads(data)
            # print(js)
            for i in js:
                k+=1
                frends_list.append(i)
    return frends_list


frends_list=get_Frends_list()
print(frends_list)
