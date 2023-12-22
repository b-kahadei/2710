import os
from pprint import pprint

stop_list = ["venv", ".git"]
for dir in os.listdir():
    print(dir)
    if dir in stop_list:
        continue
    else:
        if os.path.isdir(dir):
            pprint(list(os.walk(dir)))
            
            
