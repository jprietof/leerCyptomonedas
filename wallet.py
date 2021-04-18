import requests

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '044da392-e920-48af-8aed-b31409241b83'
}

def moneda(crypto):
    return crypto in monedas


monedas = ()
monedas_dic = {}

data = requests.get(url, headers=headers).json()
for id in data["data"]:
    monedas_dic[id["symbol"]] = id["quote"]["USD"]["price"]

monedas = monedas_dic.keys()

coin = input("Ingrese la iniciales de la moneda: ").upper()
while not moneda(coin):
    print("Moneda Invalida")
    coin = input("Ingrese la iniciales de las monedas: ").upper()
else:
    print("La moneda con symbol:", coin, "Tiene un precio de:", monedas_dic.get(coin), "USD")