
class DispensadorEfectivo:

    def __init__(self):
        
        self.__CUENTA_INICIAL = 500
        self.__cuenta = 500


    def dispensarEfectivo(self, monto):

        self.__cuenta -= (monto // 20)


    def haySuficienteEfectivoDisponible(self, monto):

        return self.__cuenta >= monto // 20

