# Импорт функцій до головного Main файлу
from src.loader import *
from src.cleaning import *
from src.union import *
from src.transform import *
from sql.to_sql import *
from googlesh.to_gs import to_googleshts

# Збираємо таблиці до єдиного джерела
loader_6 = loader_data_6_tables()
loader_post4 = loader_data_2()
loader_wether = loader_data_3()

# Форматуємо до єдиного зразку усі три таблиці
clean_6 = clean_6_month(loader_6)
clean_4 = clean_posta4(loader_post4)
clean_weth = clean_weather(loader_wether)

# Робипо додавання таблиць одного до одної
datafreame_union_6 = union_concat_6t(clean_6)
datafreame_posta4 = union_posta4(clean_4)

# Робимо поєднання таблиць по ключах
merge_table = merge_first(datafreame_union_6, clean_weth)
global_table_ = merge_all(datafreame_posta4, merge_table)

global_table = clean_fillna(global_table_)

# Підрахунки, та додавання нових стовбців
global_table = datetime(global_table)
global_table = nebalans(global_table)
global_table = dodatkovi_vutratu(global_table)

# Загружаємо до SQL та Google Sheats
to_sql = from_python_to_sql(global_table)
to_GS = to_googleshts(global_table)

print('Скрипт завантажен та працює...!')