from .pantalla import Pantalla
from .teclado import Teclado
from .dispensador_efectivo import DispensadorEfectivo
from .ranura_deposito import RanuraDeposito
from .base_datos_banco import BaseDatosBanco
from .solicitud_saldo import SolicitudSaldo
from .retiro import Retiro
from .deposito import Deposito

from enum import Enum


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
        
        if tipo == OpcionMenu.SOLICITUD_SALDO:

            return SolicitudSaldo(
                self.__numero_cuenta_actual, 
                self.__pantalla, 
                self.__baseDatosBanco
            )

        if tipo == OpcionMenu.RETIRO:

            return Retiro(
                self.__numero_cuenta_actual,
                self.__pantalla,
                self.__baseDatosBanco,
                self.__teclado,
                self.__dispensador_efectivo
            )

        if tipo == OpcionMenu.DEPOSITO:

            return Deposito(
                self.__numero_cuenta_actual,
                self.__pantalla,
                self.__baseDatosBanco,
                self.__teclado,
                self.__ranura_deposito
            )


    def __AutenticarUsuario(self):

        self.__pantalla.mostrarMensaje("\nEscriba su numero de cuenta: ")
        numeroCuenta = self.__teclado.obtenerEntrada()
        self.__pantalla.mostrarMensaje("\nEscriba su NIP: ")
        nip = self.__teclado.obtenerEntrada()

        usuarioAutenticado = self.__baseDatosBanco.autenticarUsuario(numeroCuenta, nip)

        if self.__usuario_autentificado:
        
            self.__numero_cuenta_actual = numeroCuenta
        
        else:
            self.__pantalla.mostrarLineaMensaje("Numero de cuenta o NIP invalido. Intente de nuevo.")


    def __RealizarTransacciones(self):

        usuarioSalio = False

        while not usuarioSalio:

            seleccionMenuPrincipal = self.__MostrarMenuPrincipal()
            transacciones = (OpcionMenu.SOLICITUD_SALDO, OpcionMenu.RETIRO, OpcionMenu.DEPOSITO)

            if seleccionMenuPrincipal in transacciones:

                transaccionActualPtr = self.__CrearTransaccion(seleccionMenuPrincipal)
                transaccionActualPtr.Ejecutar()
            
            elif seleccionMenuPrincipal == OpcionMenu.SALIR:

                self.__pantalla.mostrarLineaMensaje("\nSaliendo del sistema...")
                usuarioSalio = True
                break
            
            else:

                self.__pantalla.mostrarLineaMensaje("\nNo introdujo una seleccion valida. Intente de nuevo.")
                break


    def __MostrarMenuPrincipal(self):

        self.__pantalla.mostrarLineaMensaje("\nMenu principal:")
        self.__pantalla.mostrarLineaMensaje("1 - Ver mi saldo")
        self.__pantalla.mostrarLineaMensaje("2 - Retirar efectivo")
        self.__pantalla.mostrarLineaMensaje("3 - Depositar fondos")
        self.__pantalla.mostrarLineaMensaje("4 - Salir\n")
        self.__pantalla.mostrarMensaje("Introduzca una opcion: ")
        
        return self.__teclado.obtenerEntrada();


    def Ejecutar(self):

        while True:

            while not self.__usuario_autentificado:

                self.__pantalla.mostrarLineaMensaje("\nBienvenido")
                self.__AutenticarUsuario()
            
            self.__RealizarTransacciones()
            self.__usuario_autentificado = False
            self.__numero_cuenta_actual = 0
            self.__pantalla.mostrarLineaMensaje("\nGracias! Hasta luego!")
