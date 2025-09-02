from sqlalchemy.engine import create_engine
import pandas as pd
from getpass import getpass

# Завантаження до MySQL...
def from_python_to_sql(df):

    answer_MySql = input("Do u want to run function... download to MySql?")

    book = ['y', 'Y', 'yes', 'Yes', 'Да', 'да']
    try:
        if answer_MySql.lower() in book:
            password = getpass('I need your password: ...')
            # password = 'Dfkthmtdbxm24~'

            # mysql+mysqlconnector://<user>:<password>@<host>:<port>/<database>
            engine = create_engine(f"mysql+mysqlconnector://root:{password}@localhost:3306/shema_of_elecricity")

            df.to_sql('Заебало, одно и тоже...', con=engine, schema='shema_of_elecricity', if_exists='replace', index=False)

            # return x_table
    except:
        'must be zerodeviasion error...'