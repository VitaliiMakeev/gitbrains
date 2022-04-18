from xmltodict import parse
import requests

def corrency_rates(code):
    res = (None, None)
    text = requests.get('http://www.cbr.ru/scripts/XML_daily.asp.').text

    cbr = parse(text)

    date = cbr['ValCurs']['@Date']

    for v in cbr['ValCurs']['Valute']:
        if v['CharCode'] == code:
            res = (float(v['Value'].replace(',', '.')),  date)
    return res

print(corrency_rates('EUR'))

