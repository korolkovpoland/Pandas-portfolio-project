from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import set_with_dataframe
import gspread


# Завантаження до Google Sheats...
def to_googleshts(df):

    imput_words = input("Some words must be print, for downloads data to google spreads ...")
    book = ['Y', 'y', 'Yes', 'yes', 'да', 'Да']
    if imput_words.lower() in book:
        # Не забудь вказати дозвіл до гугл таблиці у Налаштуванні Дозвілу
        headers = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]
        url_sheet = "10lu0YLFl6fhqHx9rZRmheK-G7RaIHlOugdNeujd9fVQ"

        creds = ServiceAccountCredentials.from_json_keyfile_name(filename='googlesh\key_json.json', scopes=headers)
        autorise = gspread.authorize(credentials=creds)

        spreadsheets = autorise.open_by_key(key=url_sheet)
        sheet = spreadsheets.worksheet('Sheet_is_one')

        sheet.clear()
        set_with_dataframe(worksheet=sheet, dataframe=df)
