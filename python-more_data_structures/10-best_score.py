#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    order_dict = dict(sorted(a_dictionary.items(), key=lambda item: item[1], reverse=True))
    return list(order_dict.keys())[0]
