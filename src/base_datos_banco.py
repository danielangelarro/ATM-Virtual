from .database import DBManager


class BaseDatosBanco:

    def __init__(self):

        self.__db = DBManager('cuentas.db')

    
    def obtenerCuenta(self, cuenta):

        cuenta_db = self.__db.get_user_by_cuenta(cuenta)
        
        return None if cuenta_db is None else cuenta_db


    def autenticarUsuario(self, cuenta, npi):

        cuenta_db = self.__db.get_user_by_cuenta(cuenta)

        if cuenta_db is not None:

            return cuenta_db['npi'] == npi

        return False
    

    def obtenerSaldoDisponible(self, cuenta):

        cuenta_db = self.__db.get_user_by_cuenta(cuenta)

        return cuenta_db['sd']
    

    def obtenerSaldoTotal(self, cuenta):

        cuenta_db = self.__db.get_user_by_cuenta(cuenta)

        return cuenta_db['st']

    def abonar(self, cuenta, monto):

        cuenta_db = self.__db.get_user_by_cuenta(cuenta)
        self.__db.update_user_st(cuenta, cuenta_db['sd'] + monto)

    def cargar(self, cuenta, monto):

        cuenta_db = self.__db.get_user_by_cuenta(cuenta)
        self.__db.update_user_sd(cuenta, cuenta_db['sd'] - monto)
        self.__db.update_user_st(cuenta, cuenta_db['st'] - monto)
