import requests
from operaciones import Archivos

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

def moneda(crypto):
    return crypto in monedas

def connectApi(enlace):
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '044da392-e920-48af-8aed-b31409241b83'
    }
    info = requests.get(enlace, headers=headers).json()
    return info


monedas = ()
monedas_dic = {}
saldos = {}
cuenta = Archivos("cuentas.txt", "r+")

for elemento in cuenta.leerArchivo():
    campos = elemento.replace("\n", "").split(":")
    saldos[campos[0]]=campos[1]
cuenta.cerrarArchivo()
print(saldos.get("BTC"))

data = connectApi(url)

for id in data["data"]:
    monedas_dic[id["symbol"]] = id["quote"]["USD"]["price"]

monedas = monedas_dic.keys()
coin = input("Ingrese la iniciales de la moneda: ").upper()
cant = float(input("Ingrese la cantidas en USD: "))

while not moneda(coin):
    print("Moneda Invalida")
    coin = input("Ingrese la iniciales de las monedas: ").upper()
    cant = float(input("Ingrese la cantidas en USD: "))
else:
    print("La moneda", coin, "Tiene un precio de:", monedas_dic.get(coin), "USD")
    valor = cant / monedas_dic.get(coin)
    valorCoin = round(valor, 8)
    print(valorCoin, "BTC")
    # pueba para saldo
    valorTotal = float(saldos.get(coin)) + float(valorCoin)  # add cant
    valorTotal1 = float(saldos.get(coin)) - float(valorCoin)  # restar cant

    print(valorTotal)
    print(valorTotal1)
