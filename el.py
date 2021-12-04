# -*- coding: utf-8 -*-
import json
import requests
import chardet
from os import listdir,path
head = {'user-agent': 'semeval_8_2022_ia_downloader (+http://www.euagendas.org/semeval2022)'}
for d1 in listdir('final'):
    for file in listdir(path.join('final', d1)):
        if file[-4:] != 'json':
            continue
        with open(path.join('final', d1, file),'r') as f:
            data = json.load(f)
        data ='query='+data['text']
        data = data.replace(";"," ")
        #data=data.encode('utf-8','ignore').decode("utf-8")
        response = requests.get(url='https://opentapioca.org/api/annotate',
                            headers=head,
                            data=data)
        response_json = json.loads(response.text)
        with open("test.json",'w') as f:
            json.dump(response_json,f)
        with open(path.join('final', d1, file[:-5]+'.txt'),'w',encoding='UTF-8') as f:
            for annotation in response_json['annotations']:
                f.write(annotation['tags'][0]['id']+','+annotation['tags'][0]['label'][0]+','+str(annotation['tags'][0]['score'])+'\n')
        exit()

        
