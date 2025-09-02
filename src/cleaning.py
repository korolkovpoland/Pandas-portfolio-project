# """Сбірка 6-х аркушів до одного формату
#   Та обробка данів"""
import pandas as pd


def clean_6_month(book):

    def drop(var):
        var = var.drop(index=[0,1])
        return var
    
    def ffill(var):
        var['Unnamed: 0'] = var['Unnamed: 0'].ffill()
        return var

    def split(var):
        var['Unnamed: 1'] = var['Unnamed: 1'].str.split(' - ', n=1).str[1]
        return var

    def rename(var):
        var.rename(columns={
        'Unnamed: 0': 'Date',
        'Unnamed: 1': 'Time',
        'Ціна РДН (грн/МВт*год) / DAM price, PDAM  (UAH/MWh)': 'Ціна РДН',
        'Ціна платежу за позитивний небаланс (грн/МВт*год) / Positive imbalance payment price  (UAH/MWh)': 'Позитивний небаланс',
        'Ціна платежу за негативний небаланс (грн/МВт*год) / Negative imbalance payment price  (UAH/MWh)': 'Негативний небаланс'
        }, inplace=True)
        return var

    def name(var):
        var['DateTime'] = pd.to_datetime(var['Date'].astype(str) + ' ' + var['Time'])
        var = var[['DateTime', 'Ціна РДН', 'Позитивний небаланс', 'Негативний небаланс']]
        return var

    functions = [drop, ffill, split, rename, name]
    cleaned = []

    for df in book:
        for funk in functions:
            df = funk(df)
        cleaned.append(df)
    return cleaned


def clean_posta4(note):

    post4 = []
    for var in note:
        var['DateTime'] = pd.to_datetime(var['Unnamed: 0'].astype('str') +' '+ var['Unnamed: 1'])
        var = var[['DateTime', 'Закупівля, кВт.г', 'Фактичні обсяги споживання, кВт.г']]
        post4.append(var)
    return post4


def clean_weather(culer):
    culer.drop(index=range(0,9), inplace=True)
    culer.rename(columns={
    'location': 'DateTime',
    'Базель': 'Culer'
    },inplace=True)
    culer['DateTime'] = pd.to_datetime(culer['DateTime'])
    return culer


def clean_fillna(clean_col):
    clean_col.fillna({
    'Ціна РДН': clean_col['Ціна РДН'].mean(),
    'Позитивний небаланс': clean_col['Позитивний небаланс'].mean(),
    'Негативний небаланс': clean_col['Негативний небаланс'].median()
    }, inplace=True)
    clean_col['Culer'] = clean_col['Culer'].ffill()
    return clean_col