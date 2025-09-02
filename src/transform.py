# Калькуляція, та підрахунки...
def datetime(df):
    df[['Date', 'Time']] = df['DateTime'].astype('str').str.split(' ', n=1, expand=True)
    return df

def nebalans(df):
    df['Небаланс'] = df['Фактичні обсяги споживання, кВт.г'] - df['Закупівля, кВт.г']
    return df

def calculate(df):
    if df['Фактичні обсяги споживання, кВт.г'] >= df['Закупівля, кВт.г']:
        return (df['Ціна РДН'] - df['Позитивний небаланс']) / 1000 * df['Небаланс']
    else:
        return (df['Ціна РДН'] - df['Негативний небаланс']) / 1000 * df['Небаланс']
    
def dodatkovi_vutratu(df):
    df['Додаткові витрати'] = df.apply(calculate, axis='columns')
    return df

