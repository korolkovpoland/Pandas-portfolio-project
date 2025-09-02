import pandas as pd

# Завантажуємо дані з таблиць
def loader_data_6_tables():
    df1 = pd.read_excel('Збір даних за 6 місяців\Faktychni-tsiny-nebalansiv-01-31.01.2025ukr_eng.xlsx', engine='openpyxl')
    df2 = pd.read_excel('Збір даних за 6 місяців\Faktychni-tsiny-nebalansiv-01-28.02.2025ukr_eng.xlsx', engine='openpyxl')
    df3 = pd.read_excel('Збір даних за 6 місяців\Faktychni-tsiny-nebalansiv-01-31.03.2025ukr_eng.xlsx', engine='openpyxl')
    df4 = pd.read_excel('Збір даних за 6 місяців\Faktychni-tsiny-nebalansiv-01-30.04.2025ukr_eng.xlsx', engine='openpyxl')
    df5 = pd.read_excel('Збір даних за 6 місяців\Faktychni-tsiny-nebalansiv-01-31.05.2025ukr_eng.xlsx', engine='openpyxl')
    df6 = pd.read_excel('Збір даних за 6 місяців\Faktychni-tsiny-nebalansiv-01-30.06.2025ukr_eng.xlsx', engine='openpyxl')
    return [df1, df2, df3 ,df4, df5, df6]


def loader_data_2():
    df_u1 = pd.read_excel('Збір даних за 6 місяців\Тестове завдання.xlsx', sheet_name='Постачальник 1', engine='openpyxl')
    df_u2 = pd.read_excel('Збір даних за 6 місяців\Тестове завдання.xlsx', sheet_name='Постачальник 2', engine='openpyxl')
    return [df_u1, df_u2]


def loader_data_3():
    df_wt = pd.read_excel('Збір даних за 6 місяців\Погода_почасовка.xlsx', engine='openpyxl')
    return df_wt 