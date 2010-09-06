# coding=utf-8

import re

SELECTOR = '^\s*([#-_\.a-z\s:\(\)]+?)\s*({)'
PROPERTIES = '^\s*([-a-z]*?\s*:?\s*.*?)\s*(})'
SELECTOR_SEPARATOR = ','
PROPERTIES_SEPARATOR = ';'

def finder(text, regex, sep):
    find = re.match(regex, text, re.IGNORECASE)
    if find:
        items = [i.strip() for i in find.group(1).split(sep) if i.strip()]
        return items, find.end(2)
    else:
        return find

def selector(text):
    return finder(text, SELECTOR, SELECTOR_SEPARATOR)
        
def propertie(text):
    return finder(text, PROPERTIES, PROPERTIES_SEPARATOR)

def semantictree(text, semantic=None):
    semantic = [] if semantic is None else semantic
    next = selector(text)
    if next:
        selectors, selectorlast = next
        properties, propertylast = propertie(text[selectorlast:])
        semantic.append([selectors, properties])
        return semantictree(text[selectorlast+propertylast:], semantic)
    else:
        return semantic