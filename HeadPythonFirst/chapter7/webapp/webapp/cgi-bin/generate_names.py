#! /usr/local/bin/python3
import json
import athletemodel
import yate

names = athletemodel.get_names_from_store()

print(yate_start_response("application/json"))

print(json.dumps(sorted(names)))
