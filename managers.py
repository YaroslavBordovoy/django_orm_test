import sqlite3

from models import LiteraryFormat


class LiteraryFormatManager:

    def __init__(self) -> None:
        self._connection = sqlite3.connect('library_db.sqlite')

    def get_all(self):
        literary_format_cursor = self._connection.execute(
            "SELECT * FROM literary_formats"
        )
        # print(literary_format_cursor)
        # for row in literary_format_cursor:
        #     print(row)
        return [LiteraryFormat(*row) for row in literary_format_cursor]


if __name__ == '__main__':
    manager = LiteraryFormatManager()
    print(manager.get_all())
