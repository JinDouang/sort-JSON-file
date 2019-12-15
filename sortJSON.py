import sys
import json

with open(sys.argv[1], 'r') as my_file:
    with open(my_file.name) as data_file:  
        data = json.load(data_file)
f = open(my_file.name + '.sorted', 'w+')
f.write(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))