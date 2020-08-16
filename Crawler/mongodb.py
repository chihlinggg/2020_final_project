# -*- coding: utf-8 -*-
import json

ids = []
with open('record.json', 'r') as f:
    record = json.load(f)

with open('record2.json', 'r') as f:
    record2 = json.load(f)

for data in record2:
  if data not in record:
    print (data)
#with open("record2.json","w") as f:
#  for data in output:
#    ids.append(data['comment_id'])
#  json.dump(ids,f)
#  print ('finish')

#with open('record.json', 'r') as f:
#    output = json.load(f)
#    print (output)