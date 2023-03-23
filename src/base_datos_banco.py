from .database import DBManager


class BaseDatosBanco:

    def __init__(self):

        self._db = DBManager('cuentas.db')

    
    def obtenerCuenta(self, cuenta):

        cuenta_db = self._db.get_user_by_cuenta(cuenta)
        
        return None if cuenta_db is None else cuenta_db


    def autenticarUsuario(self, cuenta, npi) -> bool:

        cuenta_db = self._db.get_user_by_cuenta(cuenta)

        if cuenta_db is not None:

            return (cuenta_db['npi'] == npi)

        return False
    

    def obtenerSaldoDisponible(self, cuenta):

        cuenta_db = self._db.get_user_by_cuenta(cuenta)

        return cuenta_db['saldoDisponible']
    

    def obtenerSaldoTotal(self, cuenta):

        cuenta_db = self._db.get_user_by_cuenta(cuenta)

        return cuenta_db['saldoTotal']

    def abonar(self, cuenta, monto):

        cuenta_db = self._db.get_user_by_cuenta(cuenta)
        self._db.update_user_st(cuenta, cuenta_db['saldoDisponible'] + monto)

    def cargar(self, cuenta, monto):

        cuenta_db = self._db.get_user_by_cuenta(cuenta)
        self._db.update_user_sd(cuenta, cuenta_db['saldoDisponible'] - monto)
        self._db.update_user_st(cuenta, cuenta_db['saldoTotal'] - monto)
