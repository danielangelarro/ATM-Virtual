
class Transaccion:

    def __init__(self, cuenta, pantalla, db):
        
        self.__numero_cuenta = cuenta
        self.__pantalla = pantalla
        self.__db = db


    def obtenerNumeroCuenta(self):

        return self.__numero_cuenta
    

    def obtenerPantalla(self):

        return self.__pantalla
    

    def obtenerBaseDatosBanco(self):

        return self.__db
