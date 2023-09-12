#!/usr/bin/python3

"""
that adds all arguments to a Python list, and then save them to a file
"""
import json
import sys
filename = "add_item.json"

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    data = load_from_json_file(filename)
except FileNotFoundError:
    data = []

for arg in sys.argv[1:]:
    data.append(arg)

save_to_json_file(data, filename)
