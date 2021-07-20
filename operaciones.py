class Archivos(object):
    def __init__(self, ruta, permisos):
        self.ruta = ruta
        self.permisos = permisos
        self.archivo = open(self.ruta, self.permisos, encoding="utf8")

    def leer_archivo(self):
        ver_doc = self.archivo.read()
        return ver_doc

    def escribir_archivo(self, texto):
        self.archivo.write(texto)

    def cerrar_archivo(self):
        self.archivo.close()
