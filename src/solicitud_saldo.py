from .transaccion import Transaccion
from .pantalla import Pantalla
from .base_datos_banco import BaseDatosBanco

import curses


class SolicitudSaldo(Transaccion):

    def __init__(self, cuenta, pantalla, db):
        
        super().__init__(cuenta, pantalla, db)
    

    def ejecutar(self):

        baseDatosBanco = super().obtenerBaseDatosBanco()
        pantalla = super().obtenerPantalla()

        saldoDisponible = baseDatosBanco.obtenerSaldoDisponible(super().obtenerNumeroCuenta())
        saldoTotal = baseDatosBanco.obtenerSaldoTotal(super().obtenerNumeroCuenta())

        # pantalla.borrarPantalla()
        # pantalla.mostrarLineaMensaje("\nInformacion de saldo:")
        # pantalla.mostrarMensaje(" - Saldo disponible: ")
        # pantalla.mostrarMontoDolares(saldoDisponible)
        # pantalla.mostrarMensaje("\n - Saldo total: ")
        # pantalla.mostrarMontoDolares(saldoTotal)
        # pantalla.mostrarLineaMensaje("")

        pantalla.guardarSaldo(saldoDisponible, saldoTotal)
        curses.wrapper(pantalla.mostrarSaldo)
