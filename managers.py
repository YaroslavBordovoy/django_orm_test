import sqlite3

from models import LiteraryFormat


class LiteraryFormatManager:

    def __init__(self) -> None:
        self._connection = sqlite3.connect('library_db.sqlite')
        self.table_name = 'literary_formats'

    def create(self, format_: str):
        self._connection.execute(
            f"INSERT INTO {self.table_name} (format) VALUES (?)",
            (format_,)
        )
        self._connection.commit()

    def get_all(self):
        literary_format_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        # print(literary_format_cursor)
        # for row in literary_format_cursor:
        #     print(row)
        return [LiteraryFormat(*row) for row in literary_format_cursor]

    def update(self, id_to_update: int, new_format: str):
        self._connection.execute(
            f"UPDATE {self.table_name} SET format = ? "
            f"WHERE id = ?",
            (new_format, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int):
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()


if __name__ == '__main__':
    manager = LiteraryFormatManager()
    manager.delete(14)
    print(manager.get_all())
