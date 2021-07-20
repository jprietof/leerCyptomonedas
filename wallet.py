import json
from datetime import datetime

import requests
from operaciones import Archivos

#  data connection
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"


def connect_api(enlace):
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '044da392-e920-48af-8aed-b31409241b83'
    }
    info = requests.get(enlace, headers=headers).json()
    return info


# check user

def code_user():
    # code users
    data_wallet = file_wallet()
    for wallet in data_wallet["data"]:
        codigos.append(wallet["codigo"])


def check_user(code, coin):
    code_user()
    data_wallet = file_wallet()
    if code in codigos:
        position = codigos.index(code)
        for cuentass in data_wallet['data'][position]["monedas"]:
            monedas_dic[cuentass['moneda']] = cuentass['saldo']

        if coin in monedas_dic.keys():
            saldo = monedas_dic[coin]
            return saldo
        else:
            return print(f"El destinatario no tiene la moneda: {coin}\n")
    else:
        return print("Upss el código no existe\n")


def saldo_remitente(moneda):
    contador = 0
    pocicicion = 0
    for number in monedas_dic:
        if moneda == number:
            pocicicion = contador
            break
        contador += 1
    return pocicicion


# check wallet

def mi_wallet(coin):
    wallet_coin()
    if coin in my_coin.keys():
        saldo_cuenta = my_coin[coin]
        return saldo_cuenta  # return saldo de my cuenta
    else:
        return False


def wallet_user(coin):
    wallet_coin()
    contador = 0
    pocicion = 0
    for number in my_coin:
        if coin == number:
            pocicion = contador
            break
        contador += 1
    return pocicion  # retorna posición de la moneda


def wallet_coin():
    # monedas wallet
    data_wallet = file_wallet()
    for cuentas in data_wallet["data"][0]["monedas"]:
        my_coin[cuentas['moneda']] = cuentas['saldo']

# save data


def cambios_wallet(data1, val1, valor):
    # global dataWallet
    data_wallet = file_wallet()
    data_wallet["data"][data1]["monedas"][val1]["saldo"] = valor
    my_file = open("cuentas.json", "w")
    json.dump(data_wallet, my_file, indent=2)
    my_file.close()


def procesar_info(codigo, moneda, destino, cuenta, movimiento, valor, monto):
    code_user()
    data1 = codigos.index(codigo)
    val1 = saldo_remitente(moneda)
    val2 = wallet_user(moneda)
    cambios_wallet(data1, val1, destino)
    cambios_wallet(0, val2, cuenta)
    date = houre.strftime("%d %B %Y a las %H: %M")
    transaccion = str(date) + " " + str(moneda) + " " + movimiento + " " + str(codigo) + " " + str(valor) \
                                                + " " + str(monto) + " USD\n"
    grabar = Archivos("movimientos.txt", "a")
    grabar.escribir_archivo(transaccion)
    grabar.cerrar_archivo()
    print("Operación realizada con exito")

# Option Menu


def recibir(moneda, monto, codigo):
    destino = check_user(codigo, moneda)
    cuenta = mi_wallet(moneda)
    # si destino es True y valor <= saldo y cuenta es True
    if type(destino) == float and type(cuenta) == float:
        valor = round((monto * 1) / coinDollar[moneda][1], 8)
        if valor <= destino:
            new_cash = round(cuenta + valor, 8)
            send_cash = round(destino - valor, 8)
            print("-------------------------------------")
            # show date of the coin
            procesar_info(codigo, moneda, send_cash, new_cash, "Recibir Cantidad", valor, monto)
        else:
            return print("El remitente sin saldo sufiente para realizar la transacción")
    elif type(destino) == float and not type(cuenta) == float:
        return print(f"En tu billetera no exite la moneda: {moneda}\n")


def enviar(moneda, monto, codigo):
    destino = check_user(codigo, moneda)
    cuenta = mi_wallet(moneda)
    if type(destino) == float and type(cuenta) == float:
        valor = round((monto * 1) / coinDollar[moneda][1], 8)
        if valor <= cuenta:
            send_cash = round(destino + valor, 8)
            new_cash = round(cuenta - valor, 8)
            # show date of the coin
            procesar_info(codigo, moneda, send_cash, new_cash, "Enviar Cantidad", valor, monto)
        else:
            return print("saldo insuficiente para realizar la operación")
    elif type(destino) == float and not type(cuenta) == float:
        return print(f"En tu billetera no exite la moneda: {moneda}\n")


def balance(coin):
    wallet_coin()
    mi_cuenta = mi_wallet(coin)
    if type(mi_cuenta) == float:
        nombre = coinDollar[coin][0]
        dollar = round(mi_cuenta * coinDollar[coin][1], 2)
        print("---------------------------------------------")
        print("Moneda\t | \tCantidad\t | \tMonto USD")
        print(f"{nombre}\t | \t{mi_cuenta}\t | \t{dollar} USD")
        print("---------------------------------------------")
    else:
        print(f"La moneda {coin} no esta en la cuenta\n")


def balance_general():
    wallet_coin()  # call function
    total = 0
    print(f"\nMoneda \t|\t Cantidad \t|\t Monto USD\n")
    for cuenta in my_coin:
        dollar = round(my_coin[cuenta] * coinDollar[cuenta][1], 2)
        total += dollar
        print(f"{cuenta} \t|\t {my_coin[cuenta]} \t|\t {dollar} USD")
        print("-------------------------------------------------------")
    print(f"\n==> EL monto total en USD de todas las monedas es de: {total} USD <==\n")


def transacciones():
    document = Archivos("movimientos.txt", "r")  # read file movimientos.txt
    print(document.leer_archivo())
    document.cerrar_archivo()


def file_wallet():
    # open file json
    a_file = open("cuentas.json", "r")
    data_wallet = json.load(a_file)
    a_file.close()
    return data_wallet


def menu():
    estado = False
    while not estado:
        print("********* Menú de Opciones *********")
        print("""
        1. Recibir Cantidad
        2. Tranferir monto
        3. Mostrar balance de una moneda
        4. Mostar balance general
        5. Mostrar historico de transaciones
        6. Salir del programa""")
        opcion = int(input("\nIngrese una opción del menu: "))
        if opcion == 1:
            moneda = input("Ingrese las iniciales de la criptomoneda a recibir: ").upper()
            monto = input("Ingrese el monto en dolares a recibir: ")
            codigo = input("Ingrese el codigo del remitente: ")
            print("____________________________________________________________________________")
            if not moneda.isdigit() and monto.isdigit() and codigo.isdigit():
                recibir(moneda, float(monto), codigo)
            else:
                print("Ingrese datos validos en cada campo")
        elif opcion == 2:
            moneda = input("Ingrese las iniciales de la criptomoneda a enviar: ").upper()
            monto = input("Ingrese el monto en dolares a enviar: ")
            codigo = input("Ingrese el codigo del destinatario: ")
            print("____________________________________________________________________________")
            if not moneda.isdigit() and monto.isdigit() and codigo.isdigit():
                enviar(moneda, float(monto), codigo)
            else:
                print("Ingrese datos validos en cada campo")
        elif opcion == 3:
            moneda = input("Ingrese la iniciales de la criptomoneda que desea consultar: ").upper()
            print("________________________________________________________________________________")
            if not moneda.isdigit():
                balance(moneda)
            else:
                print("No se permiten números\n")
        elif opcion == 4:
            balance_general()
        elif opcion == 5:
            transacciones()
        elif opcion == 6:
            estado = True
        else:
            print("| --------> Ingrese una opción correcta <---------- |\n")


houre = datetime.now()
codigos = []
monedas_dic = {}
my_coin = {}
coinDollar = {}
dataApi = connect_api(url)

# get data crypto API Coin market
for num in dataApi["data"]:
    coinDollar[num["symbol"]] = [num["name"], num["quote"]["USD"]["price"]]

menu()
