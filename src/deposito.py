from .transaccion import Transaccion
from .pantalla import Pantalla
from .base_datos_banco import BaseDatosBanco
from .teclado import Teclado
from .ranura_deposito import RanuraDeposito


CANCEL01 = 0


class Deposito(Transaccion):

    def __init__(self, cuenta, pantalla, db, teclado, ranura):

        super().__init__(cuenta, pantalla, db)

        self.__monto = 0
        self.__teclado = teclado
        self.__ranura_deposito = ranura
    

    def __pedirMontoADepositar(self):

        pantalla = super().obtenerPantalla()

        while True:
            pantalla.borrarPantalla()
            pantalla.mostrarMensaje("\nIntroduzca un monto a depositar en CENTAVOS (o 0 para cancelar): ");

            try:
                entrada = self.__teclado.obtenerEntrada()
                break
            except Exception:
                pantalla.mostrarError('No es un numero valido!!')
                aux = input()

        return CANCEL01 if entrada == CANCEL01 else entrada / 100


    def ejecutar(self):

        baseDatosBanco = super().obtenerBaseDatosBanco()
        pantalla = super().obtenerPantalla()

        self.__monto = self.__pedirMontoADepositar()

        if self.__monto is not CANCEL01:

            pantalla.mostrarMensaje(f"\nInserte un sobre de deposito que contenga {self.__monto} en la ranura de deposito.")

            sobreRecibido = self.__ranura_deposito.seRecibioSobre()

            if sobreRecibido:

                pantalla.mostrarLineaMensaje("\nSe recibio su sobre." \
                                "\nNOTA: El dinero depositado no estara disponible sino hasta" \
                                "\nverificar el monto de cualquier efectivo incluido, junto con " \
                                "los cheques.")

                baseDatosBanco.abonar(super().obtenerNumeroCuenta(), self.__monto);

            else:

                pantalla.mostrarLineaMensaje("\nUsted no inserto un sobre, por lo que el ATM CANCELO su transaccion.");
