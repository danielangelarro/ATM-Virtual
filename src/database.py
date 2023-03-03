from enum import IntEnum
from typing import Optional, List
import sqlite3


class DBManager:
    def __init__(self, db_path: str) -> None:
        self.db = sqlite3.connect(
            db_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
            check_same_thread=False)
        self.db.row_factory = sqlite3.Row
        self.execute(
            '''CREATE TABLE IF NOT EXISTS users
            (cuenta TEXT PRIMARY KEY,
            name TEXT,
            npi TEXT,
            saldoDisponible FLOAT,
            saldoTotal FLOAT)''')
    
    def execute(self, statement: str, args=()) -> sqlite3.Cursor:
        return self.db.execute(statement, args)

    def commit(self, statement: str, args=()) -> sqlite3.Cursor:
        with self.db:
            return self.db.execute(statement, args)
    
    def close(self) -> None:
        self.db.close()

    # ==== users =====

    def add_user(self, gid: int, name: str, cuenta: str, npi: str, sd: float, st: float) -> None:
        self.commit('INSERT INTO users VALUES (?,?,?,?,?)',
                    (cuenta, name, npi, sd, st))
    
    def update_user_sd(self, cuenta: str, monto) -> None:
        self.commit('UPDATE users SET sd=? WHERE cuenta=?', (monto, cuenta))

    def update_user_st(self, cuenta: str, monto) -> None:
        self.commit('UPDATE users SET st=? WHERE cuenta=?', (monto, cuenta))

    def remove_user(self, cuenta: str) -> None:
        self.commit('DELETE FROM users WHERE cuenta=?', (cuenta,))

    def get_user_by_cuenta(self, cuenta: str) -> Optional[sqlite3.Row]:
        return self.execute(
            'SELECT * FROM users WHERE cuenta=?', (cuenta,)).fetchone()
    
    def get_user_by_name(self, name: str) -> Optional[sqlite3.Row]:
        return self.execute(
            'SELECT * FROM users WHERE name=?', (name,)).fetchone()

    def get_users(self) -> List[sqlite3.Row]:
        return self.execute(
            'SELECT * FROM users').fetchall()
