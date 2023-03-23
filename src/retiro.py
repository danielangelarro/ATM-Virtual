from .transaccion import Transaccion
from .pantalla import Pantalla
from .base_datos_banco import BaseDatosBanco
from .teclado import Teclado
from .dispensador_efectivo import DispensadorEfectivo

import curses


CANCELO = 6;


class Retiro(Transaccion):

    def __init__(self, cuenta, pantalla, db, teclado, dispensador):
        
        super().__init__(cuenta, pantalla, db)

        self.__monto = 0
        self.__teclado = teclado
        self.__dispensador_efectivo = dispensador
    

    def __mostrarMenuDeMontos(self):

        opcionUsuario = 0
        pantalla = super().obtenerPantalla()

        montos = [0, 20, 40, 60, 100, 200]

        while opcionUsuario == 0:

            # pantalla.borrarPantalla()
            # pantalla.mostrarLineaMensaje("\nOpciones de retiro:")
            # pantalla.mostrarLineaMensaje("1 - $20")
            # pantalla.mostrarLineaMensaje("2 - $40")
            # pantalla.mostrarLineaMensaje("3 - $60")
            # pantalla.mostrarLineaMensaje("4 - $100")
            # pantalla.mostrarLineaMensaje("5 - $200")
            # pantalla.mostrarLineaMensaje("6 - Cancelar transaccion")
            # pantalla.mostrarMensaje("\nElija una opcion de retiro (1-6): ")

            # entrada = self.__teclado.obtenerEntrada()
            entrada = curses.wrapper(pantalla.mostrarRetiro)

            if entrada in (1, 2, 3, 4, 5):

                opcionUsuario = montos[entrada]
                break
            
            elif entrada == CANCELO:

                opcionUsuario = CANCELO
            
            else:

                pantalla.mostrarLineaMensaje("\nSeleccion invalida. Intente de nuevo.")

        return opcionUsuario


    def ejecutar(self):

        repetirTrensaccion = True
        efectivoDispensado = False
        transaccionCancelada = False
        
        baseDatosBanco = super().obtenerBaseDatosBanco()
        pantalla = super().obtenerPantalla()

        while repetirTrensaccion and (not efectivoDispensado and not transaccionCancelada):

            pantalla.borrarPantalla()
            seleccion = self.__mostrarMenuDeMontos()

            if seleccion is not CANCELO:

                self.__monto = seleccion
                saldoDisponible = baseDatosBanco.obtenerSaldoDisponible(super().obtenerNumeroCuenta())

                if self.__monto <= saldoDisponible:
                    
                    if self.__dispensador_efectivo.haySuficienteEfectivoDisponible(self.__monto):

                        baseDatosBanco.cargar(super().obtenerNumeroCuenta(), self.__monto)
                        self.__dispensador_efectivo.dispensarEfectivo(self.__monto)
                        efectivoDispensado = True

                        pantalla.mostrarLineaMensaje("\nPor favor tome su efectivo del dispensador de efectivo.")
                    
                    else:

                        pantalla.mostrarLineaMensaje("\nNo hay suficiente efectivo disponible en el ATM.\n\nElija un monto menor.")
                
                else:

                    pantalla.mostrarLineaMensaje("Dinero insuficiente.\nCancelando la transaccion...\n\nPresione una tecla para continuar...")
                    transaccionCancelada = True

            else: 
                repetirTrensaccion = False

