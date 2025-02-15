#!/usr/bin/env python3
import json
import csv

def convert_csv_to_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reade   r)

        with open("data.json", "w", encoding="utf-8") as j_file:
            json.dump(data, j_file)
            return True
    except Exception:
        return False    
