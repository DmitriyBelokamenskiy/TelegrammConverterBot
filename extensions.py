import requests
import json
from Config import keys


class ConversionException(Exception):
    pass


class Input:

    @staticmethod
    def check_input(initial_data):

        values = str(initial_data).lower().split(' ')

        if len(values) != 3:
            raise ConversionException('Ошибка: Неверное количество параметров')

        try:
            base_ticker = keys[values[0]]
        except:
            raise ConversionException(f'Ошибка: Не удалось обработать валюту: "{values[0]}"')

        try:
            quote_ticker = keys[values[1]]
        except:
            raise ConversionException(f'Ошибка: Не удалось обработать валюту: "{values[1]}"')

        try:
            amount = float(values[2])
        except:
            raise ConversionException(f'Ошибка: Не удалось обработать количество: "{values[2]}"')

        correct_input = [base_ticker, quote_ticker, amount]

        return correct_input


class GetPrice:
    @staticmethod
    def get_price(correct_input):

        base = correct_input[0]
        quote = correct_input[1]
        amount = correct_input[2]

        if base == 'RUB':
            base_value = 1
        else:
            get_data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
            json_data = json.loads(get_data.content)
            base_value = json_data['Valute'][base]['Value']

        if quote == 'RUB':
            quote_value = 1
        else:
            get_data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
            json_data = json.loads(get_data.content)
            quote_value = json_data['Valute'][quote]['Value']

        calc = round((base_value / quote_value) * amount, 2)

        Text = f'Стоимость {amount} {base} составляет {calc} {quote}'

        return Text
