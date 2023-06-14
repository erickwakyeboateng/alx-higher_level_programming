#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    restt = list(a_dictionary.keys())[0]
    bing = a_dictionary[restt]
    for l, w in a_dictionary.items():
        if w > bing:
            bing = w
            restt = l
    return (restt)
