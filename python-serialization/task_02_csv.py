#!/usr/bin/env python3
import json
import csv

def convert_csv_to_json(filename):
    try:
        with open(filename, "r", "utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            date = list(reader)

        with open("data.json", "w", "utf-8") as j_file:
            json.dump(date, j_file)
            return True
    except Exception:
        return False    
