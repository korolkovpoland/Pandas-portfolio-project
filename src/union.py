import pandas as pd

# Поєднання таблиць у одну єдину...
def union_concat_6t(book):
    df = pd.concat(book, axis='index')
    return df

def union_posta4(table):
    df = pd.concat(table, axis='index')
    return df

def merge_first(month6, wether):
    x = pd.merge(month6, wether, how='left', on='DateTime')
    return x

def merge_all(posta4, culer):
    var = pd.merge(left=posta4, right=culer, how='left', on='DateTime')
    return var