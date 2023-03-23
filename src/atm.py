from .pantalla import Pantalla
from .teclado import Teclado
from .dispensador_efectivo import DispensadorEfectivo
from .ranura_deposito import RanuraDeposito
from .base_datos_banco import BaseDatosBanco
from .solicitud_saldo import SolicitudSaldo
from .retiro import Retiro
from .deposito import Deposito

from enum import Enum
import curses


class  OpcionMenu(Enum):
    SOLICITUD_SALDO = 1
    RETIRO = 2
    DEPOSITO = 3
    SALIR = 4


class ATM:

    def __init__(self):
        
        self.__usuario_autentificado = False
        self.__numero_cuenta_actual = 0
        self.__pantalla = Pantalla()
        self.__teclado = Teclado()
        self.__dispensador_efectivo = DispensadorEfectivo()
        self.__ranura_deposito = RanuraDeposito()
        self.__baseDatosBanco = BaseDatosBanco()


    def __CrearTransaccion(self, tipo):
        
        if tipo == 1:

            return SolicitudSaldo(
                self.__numero_cuenta_actual, 
                self.__pantalla, 
                self.__baseDatosBanco
            )

        if tipo == 2:

            return Retiro(
                self.__numero_cuenta_actual,
                self.__pantalla,
                self.__baseDatosBanco,
                self.__teclado,
                self.__dispensador_efectivo
            )

        if tipo == 3:

            return Deposito(
                self.__numero_cuenta_actual,
                self.__pantalla,
                self.__baseDatosBanco,
                self.__teclado,
                self.__ranura_deposito
            )


    def __AutenticarUsuario(self):

        # self.__pantalla.mostrarMensaje("\nEscriba su numero de cuenta: ")
        # numeroCuenta = self.__teclado.obtenerEntrada()
        # self.__pantalla.mostrarMensaje("\nEscriba su NIP: ")
        # nip = self.__teclado.obtenerEntrada()

        numeroCuenta, nip = curses.wrapper(self.__pantalla.mostrarLogin)

        self.__usuario_autentificado = self.__baseDatosBanco.autenticarUsuario(numeroCuenta, str(nip))

        if self.__usuario_autentificado:
        
            self.__numero_cuenta_actual = numeroCuenta
        
        else:
            self.__pantalla.mostrarLineaMensaje("Numero de cuenta o NIP invalido. Intente de nuevo.")


    def __RealizarTransacciones(self):

        usuarioSalio = False

        while not usuarioSalio:

            self.__pantalla.borrarPantalla()
            seleccionMenuPrincipal = self.__MostrarMenuPrincipal()
            transacciones = (1, 2, 3)

            if seleccionMenuPrincipal in transacciones:

                transaccionActualPtr = self.__CrearTransaccion(seleccionMenuPrincipal)
                transaccionActualPtr.ejecutar()
            
            elif seleccionMenuPrincipal == 4:

                self.__pantalla.mostrarLineaMensaje("\nSaliendo del sistema...")
                usuarioSalio = True
                break
            
            else:

                self.__pantalla.mostrarLineaMensaje("\nNo introdujo una seleccion valida. Intente de nuevo.")
                break

            aux = input()


    def __MostrarMenuPrincipal(self):

        # self.__pantalla.mostrarLineaMensaje("\nMenu principal:")
        # self.__pantalla.mostrarLineaMensaje("1 - Ver mi saldo")
        # self.__pantalla.mostrarLineaMensaje("2 - Retirar efectivo")
        # self.__pantalla.mostrarLineaMensaje("3 - Depositar fondos")
        # self.__pantalla.mostrarLineaMensaje("4 - Salir\n")
        # self.__pantalla.mostrarMensaje("Introduzca una opcion: ")
        
        opt = curses.wrapper(self.__pantalla.mostrarMenuInicio)

        # return self.__teclado.obtenerEntrada();
        return int(opt)


    def Ejecutar(self):

        while True:


            while not self.__usuario_autentificado:
                self.__pantalla.borrarPantalla()

                #self.__pantalla.mostrarLineaMensaje("\nBienvenido")
                
                self.__AutenticarUsuario()

                # aux = input()
            
            self.__RealizarTransacciones()
            self.__usuario_autentificado = False
            self.__numero_cuenta_actual = 0
            self.__pantalla.mostrarLineaMensaje("\nGracias! Hasta luego!")
