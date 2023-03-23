from src import BaseDatosBanco, Pantalla
from enum import Enum
from os import system


class  OpcionMenu(Enum):
    CREAR_CUENTA = 1
    ELIMINAR_CUENTA = 2
    VER_CUENTAS = 3
    SALIR = 4


MENU = '''MENU:

[1] CREAR CUENTA
[2] ELIMINAR CUENTA
[3] VER CUENTAS
[4] SALIR
'''

class Manager(BaseDatosBanco):

    def __init__(self):

        super().__init__()

        self.pantalla = Pantalla()
    
    def crearCuenta(self, name, cuenta, npi, sd, st):

        _cuenta = self.obtenerCuenta(cuenta)

        if _cuenta is None:

            self._db.add_user(name, cuenta, npi, sd, st)
            return True
            
        self.pantalla.mostrarError('El numero de cuenta ya existe.')
        return False

    def eliminarCuenta(self, cuenta):

        self._db.remove_user(cuenta)

        return True

    def verCuentas(self):

        cuenta_db = self._db.get_users()

        self.pantalla.mostrarLineaMensaje('*** CUENTAS REGISTRADAS ***')
        
        msg = '{:3s} | {:10s} | {:15s} | {:4s} | {:17s} | {:17s} |'
        msg = msg.format('No.', 'Cuenta', 'Nombre', 'Npi.', 'Saldo Disponible', 'Sa;do Total')

        self.pantalla.mostrarLineaMensaje(msg)

        for i, e in enumerate(cuenta_db):

            msg = '{:0=3d} | {:10s} | {:15s} | {:4s} | ${:16f} | ${:16f} |'
            msg = msg.format(i+1, e['cuenta'], e['name'], e['npi'], e['saldoDisponible'], e['saldoTotal'])

            self.pantalla.mostrarLineaMensaje(msg)

        return False


if __name__ == '__main__':

    manager = Manager()

    while True:
        print(MENU)

        op = input()

        if op == '1':
            system('clear')

            print('CREAR NUEVO USUARIO:\n')

            name = input('Nombre: ')
            cuenta = input('Cuenta: ')
            npi = input('Contrasenia: ')
            sd, st = 500, 500

            manager.crearCuenta(name, cuenta, npi, sd, st)
        
        elif op == '2':
            system('clear')

            print('ELIMINAR CUENTA\n')

            cuenta = input('Cuenta: ')
            manager.eliminarCuenta(cuenta)
        
        elif op == '3':
            system('clear')

            print('CUENTAS REGISTRADAS\n')
            manager.verCuentas()
        
        elif op == '4':

            break

        else:
            print('Comando invalido!!!')
        
        p = input()
        