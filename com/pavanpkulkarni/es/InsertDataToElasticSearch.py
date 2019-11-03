import requests, json, os
from elasticsearch import Elasticsearch, helpers


es = Elasticsearch('http://localhost:9200')
iinputPath = "/Users/pavanpkulkarni/Documents/ELK/sample_data"

print(os.getcwd())
print("************* Begin Loading Data *************")

for filename in os.listdir(iinputPath):
    if filename.endswith('.json'):
        print("Processing File  : ", filename)
        f = open(os.path.join(iinputPath, filename), 'r', encoding='utf-8')
        json_data = f.read()
        json.loads(json_data)
        es.index(index='travelagent', doc_type='traveldeets', body=json.loads(json_data))
print("************* End Loading Data *************")