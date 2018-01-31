import json

raw = {'rows':6, 
'cols':6, 
'start':(0,0), 
'end':(5,5), 
'walls':((0, 5), (1, 0), (1, 1), (1, 5), (2, 3), (3, 1), (3, 2), (3, 5), (4, 1), (4, 4), (5, 1))}

print raw

json_str = json.dumps(raw)
print json_str

parsed_json = json.loads(json_str)

print parsed_json['start']