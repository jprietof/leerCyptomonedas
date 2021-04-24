class Archivos(object):
    def __init__(self, ruta, permisos):
        self.ruta = ruta
        self.permisos = permisos

    def abrirArchivo(self):
        archivo = open(self.ruta, self.permisos, encoding="utf8")
        return archivo

    def leerArchivo(self):
        archivo = open(self.ruta, self.permisos, encoding="utf8")
        verDoc = archivo.readlines()
        return verDoc

    def escribirArchivo(self, texto):
        archivo = open(self.ruta, self.permisos, encoding="utf8")
        archivo.write(texto)
        return print("Registro satisfactorio")

    def cerrarArchivo(self):
        archivo = open(self.ruta, self.permisos, encoding="utf8")
        archivo.close()

class criptomendas(object):

    def __init__(self, nombre, saldo, cotizacion):
        self.nombre = nombre
        self.saldo = saldo
        self.cotizacion = cotizacion