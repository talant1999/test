import json
from urllib.request import urlopen
import ssl


# Вставил, чтобы не вылезала ошибка CERTIFICATE_VERIFY_FAILED
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


try:
    with open('goods.json') as fileJSON:
        goodsJSON = json.load(fileJSON)
    print('Данные из json файла')
    print(goodsJSON)
    sumPrice = 0
    for i in range(3):
        sumPrice += goodsJSON['goods'][i]['price']
    print('Цена товаров в рублях', sumPrice)
except Exception as exc:
    print(exc)


try:
    with urlopen("https://www.cbr-xml-daily.ru/daily_json.js") as response:
        source = response.read()
    data = json.loads(source)
    print('Данные из json файла ЦБ')
    print(data)
    priceUSD = sumPrice / data['Valute']['USD']['Value']
    print('Цена товаров в USD', priceUSD)
except Exception as exc:
    print(exc)
