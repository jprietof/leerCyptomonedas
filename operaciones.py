class Archivos(object):
    def __init__(self, ruta, permisos):
        self.ruta = ruta
        self.permisos = permisos

    def abrir_archivo(self):
        archivo = open(self.ruta, self.permisos, encoding="utf8")
        return archivo

    def leer_archivo(self):
        archivo = open(self.ruta, self.permisos, encoding="utf8")
        ver_doc = archivo.readlines()
        return ver_doc

    def escribir_archivo(self, texto):
        archivo = open(self.ruta, self.permisos, encoding="utf8")
        archivo.write(texto)
        return print("Registro satisfactorio")

    def cerrar_archivo(self):
        archivo = open(self.ruta, self.permisos, encoding="utf8")
        archivo.close()


class Criptomendas(object):

    def __init__(self, nombre, saldo, cotizacion):
        self.nombre = nombre
        self.saldo = saldo
        self.cotizacion = cotizacion
