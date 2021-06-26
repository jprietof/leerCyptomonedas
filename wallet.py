import json
import requests
from datetime import datetime
from operaciones import Archivos

#  data connection
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"


def connectApi(enlace):
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '044da392-e920-48af-8aed-b31409241b83'
    }
    info = requests.get(enlace, headers=headers).json()
    return info


saldo = 0
mensaje = ""
houre = datetime.now()


# print(round(val_actual * coinDollar[moneda], 2))

def check_user(code, coin):
    if code in codigos:
        position = codigos.index(code)
        for cuentas in dataWallet['data'][position]["monedas"]:
            monedas_dic[cuentas['moneda']] = cuentas['saldo']

        if coin in monedas_dic.keys():
            globals()['saldo'] = monedas_dic[coin]
            return True
        else:
            globals()['mensaje'] = "no tiene la moneda " + str(coin)
            return False
    else:
        globals()["mensaje"] = "no existe"
        return False


def mi_wallet(coin):
    for cuenta in dataWallet["data"][0]["monedas"]:
        my_coin[cuenta['moneda']] = cuenta['saldo']
    if coin in my_coin.keys():
        globals()["my_saldo"] = my_coin[coin]
        return True
    else:
        return False


def recibir(moneda, monto, codigo):
    destino = check_user(codigo, moneda)
    cuenta = mi_wallet(moneda)
    # si destino es True y valor <= saldo y cuenta es True
    if destino and cuenta:
        valor = round((monto * 1) / coinDollar[moneda], 8)
        if valor <= saldo:
            new_cash = round(my_saldo + valor, 8)
            send_cash = round(saldo - valor, 8)
            print(new_cash)
            print(send_cash)
            # save -> date, coin, type operation, code user, cant, cash dollar send
            date = houre.strftime("%d %B %Y a las %H: %M")
            transaccion = [date, moneda, "Recibir Cantidad", codigo, valor, str(monto) + " USD"]
            return print(transaccion)
        else:
            return print("El remitente sin saldo sufiente para realizar la transacción")
    elif destino and not cuenta:
        return print("Lo siento en tu billetera no exite la moneda: ", moneda)
    else:
        return print("El remitente", mensaje)


def enviar(moneda, monto, codigo):
    destino = check_user(codigo, moneda)
    cuenta = mi_wallet(moneda)
    if destino and cuenta:
        valor = round((monto * 1) / coinDollar[moneda], 8)
        if valor <= my_saldo:
            send_cash = round(saldo + valor, 8)
            new_cash = round(my_saldo - valor, 8)
            print(send_cash)
            print(new_cash)
            date = houre.strftime("%d %B %Y a las %H: %M")
            transaccion = [date, moneda, "Transferir Monto", codigo, valor, str(monto) + " USD"]
            return print(transaccion)
        else:
            return print("saldo insuficiente")
    elif destino and not cuenta:
        return print("Lo siento en tu billetera no exite la moneda: ", moneda)
    else:
        return print("El remitente", mensaje)


def balance():
    pass


def balance_general():
    pass


def transacciones():
    pass


codigos = []
monedas_dic = {}
my_coin = {}
my_saldo = 0
coinDollar = {}
dataApi = connectApi(url)

# get data crypto if api Coin market
for num in dataApi["data"]:
    coinDollar[num["symbol"]] = num["quote"]["USD"]["price"]

# open file json
a_file = open("cuentas.json", "r")
dataWallet = json.load(a_file)
a_file.close()

print(len(dataWallet["data"]))

for wallet in dataWallet["data"]:
    codigos.append(wallet["codigo"])

print(codigos)

"""cuenta = int(input("Ingrese el código: "))
print(cuenta)
if cuenta in codigos:
    posicion = codigos.index(cuenta)
    for saldo in dataWallet["data"][posicion]["monedas"]:
        monedas_dic[saldo["moneda"]] = saldo["saldo"]
else:
    print("La cuenta no existe")

print(monedas_dic)

crypto = input("Ingrese la criptomoneda: ")
monto = monedas_dic[crypto]
print("El saldo de", crypto, "es", monto)

# edit file json
print(dataWallet["data"][1]["monedas"][1]["moneda"])
dataWallet["data"][1]["monedas"][0]["moneda"] = "btc"
a_file = open("cuentas.json", "w")
json.dump(dataWallet, a_file, indent=2)
a_file.close() """


def menu():
    print("********* Menú de Opciones *********")
    print("""
    1. Recibir Cantidad
    2.Tranferir monto
    3. Mostrar balance de una moneda
    4. Mostar balance general
    5. Mostrar historico de transaciones
    6. Salir del programa""")
    opcion = input("\nIngrese una opción del menu: ")
    if opcion == "1":
        print("es la opcion 1")
        moneda = input("Ingrese las iniciales de la criptomoneda a recibir: ").upper()
        monto = input("Ingrese el monto en dolares a recibir: ")
        codigo = input("Ingrese el codigo del remitente: ")
        if not moneda.isdigit() and monto.isdigit() and codigo.isdigit():
            recibir(moneda, float(monto), codigo)
        else:
            print("Ingrese datos validos en cada campo")
    if opcion == "2":
        print("es la opcion 2")
        moneda = input("Ingrese las iniciales de la criptomoneda a enviar: ").upper()
        monto = input("Ingrese el monto en dolares a enviar: ")
        codigo = input("Ingrese el codigo del destinatario: ")
        if not moneda.isdigit() and monto.isdigit() and codigo.isdigit():
            enviar(moneda, float(monto), codigo)
        else:
            print("Ingrese datos validos en cada campo")


menu()
""" cuenta = Archivos("movimientos.txt", "r+")
print(cuenta.leerArchivo())
for elemento in cuenta.leerArchivo():
    campos = elemento.replace("\n", "").split(":")
    print(len(campos))
cuenta.cerrarArchivo()


data = connectApi(url)

for id in data["data"]:
    monedas_dic[id["symbol"]] = id["quote"]["USD"]["price"]

monedas = monedas_dic.keys()
cuenta.escribirArchivo(str(monedas))
print(monedas)
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
    """
