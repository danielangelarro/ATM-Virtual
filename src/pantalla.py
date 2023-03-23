import os
import curses


class Pantalla:

    def mostrarLogin(self, stdscr):
        # Clear screen
        stdscr.clear()

        # Create a menu
        menu = ['BIENVENIDO A SU ATM', ' ', 'Inserte su tarjeta para comenzar...']
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        
        stdscr.refresh()
        for i, item in enumerate(menu):
            x = int((curses.COLS - len(item)) / 2)
            y = int((curses.LINES - len(menu)) / 2) + i
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, item)
            stdscr.attroff(curses.color_pair(1))
            
        while True:
            key = stdscr.getch()
            if key == curses.KEY_ENTER or key in [10, 13]:
                break


        curses.curs_set(1)
        curses.endwin()

        self.mostrarMensaje("\nEscriba su numero de cuenta: ")
        numeroCuenta = input()
        self.mostrarMensaje("\nEscriba su NIP: ")
        nip = input()

        return numeroCuenta, nip
        
    def mostrarMenuInicio(self, stdscr):
        # Clear screen
        stdscr.clear()

        # Create a menu
        menu = ['Consultar saldo', 'Retirar efectivo', 'Depositar fondos', 'Salir']
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
        current_row = 0

        # Display the menu
        while True:
            stdscr.refresh()
            for i, item in enumerate(menu):
                x = int((curses.COLS - len(item)) / 2)
                y = int((curses.LINES - len(menu)) / 2) + i
                if i == current_row:
                    stdscr.attron(curses.color_pair(1))
                    stdscr.addstr(y, x, item)
                    stdscr.attroff(curses.color_pair(1))
                else:
                    stdscr.attron(curses.color_pair(2))
                    stdscr.addstr(y, x, item)
                    stdscr.attroff(curses.color_pair(2))
            key = stdscr.getch()
            
            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                # if current_row == len(menu) - 1:
                break

        # Exit
        curses.curs_set(1)
        curses.endwin()

        return current_row + 1

    def mostrarRetiro(self, stdscr):
        # Clear screen
        stdscr.clear()

        # Create a menu
        menu = ['OPCIONES DE RETIRO', ' ', '$20', '$40', '$60', '$100', '$200', 'Cancelar']
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
        current_row = 2

        # Display the menu
        while True:
            stdscr.refresh()
            for i, item in enumerate(menu):
                x = int((curses.COLS - len(item)) / 2)
                y = int((curses.LINES - len(menu)) / 2) + i
                if i == current_row:
                    stdscr.attron(curses.color_pair(1))
                    stdscr.addstr(y, x, item)
                    stdscr.attroff(curses.color_pair(1))
                else:
                    stdscr.attron(curses.color_pair(2))
                    stdscr.addstr(y, x, item)
                    stdscr.attroff(curses.color_pair(2))
            key = stdscr.getch()
            
            if key == curses.KEY_UP and current_row > 2:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                # if current_row == len(menu) - 1:
                break

        # Exit
        curses.curs_set(1)
        curses.endwin()

        return current_row - 1

    def guardarSaldo(self, saldoDisponible, saldoTotal):
        self.saldoDisponible = saldoDisponible
        self.saldoTotal = saldoTotal

    def mostrarSaldo(self, stdscr):
        # Clear screen
        stdscr.clear()

        # Create a menu
        menu = [
            'INFORMACION DE SALDO', ' ', 
            f'Saldo Disponible: {self.saldoDisponible}', 
            f'Saldo Total: {self.saldoTotal}', 
            ' ','Aceptar'
        ]
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
        current_row = 5

        # Display the menu
        while True:
            stdscr.refresh()
            for i, item in enumerate(menu):
                x = int((curses.COLS - len(item)) / 2)
                y = int((curses.LINES - len(menu)) / 2) + i
                if i == current_row:
                    stdscr.attron(curses.color_pair(1))
                    stdscr.addstr(y, x, item)
                    stdscr.attroff(curses.color_pair(1))
                else:
                    stdscr.attron(curses.color_pair(2))
                    stdscr.addstr(y, x, item)
                    stdscr.attroff(curses.color_pair(2))
            key = stdscr.getch()
            
            if key == curses.KEY_ENTER or key in [10, 13]:
                if current_row == len(menu) - 1:
                    break

        # Exit
        curses.curs_set(1)
        curses.endwin()

    def mostrarMensaje(self, mensaje):

        print(mensaje, end="")
    

    def mostrarLineaMensaje(self,mensaje):

        print(mensaje)

    def mostrarMontoDolares(self, monto):

        print(f'${monto}')

    def mostrarError(self, error):

        print(f'[!] {error}')
    
    def borrarPantalla(self):

        os.system('clear')