import sqlite3


class db_help:
    def __init__(self, db_name):
        """Method to init database"""

        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(e)

    def add_info(self, table, column, question):
        """Method to add new question into our table"""
        a = "'" + "', '".join(question) + "'"
        column_formatted = ', '.join(column)
        print("INSERT OR IGNORE INTO {table} ({column}) VALUES ({quest})".format(table=table, column=column_formatted,
                                                                               quest=a))
        self.cursor.execute(
            "INSERT OR IGNORE INTO {table} ({column}) VALUES ({quest})".format(table=table, column=column_formatted,
                                                                               quest=a))

        self.conn.commit()

    def return_info(self, where, what='*'):
        """This method is counting percent of '+'"""

        return self.cursor.execute("SELECT {what} FROM {where}".format(what=what, where=where)).fetchall()

    def close(self):
        if self.conn:
            self.conn.close()

    def add_info_full(self, table, question):
        """Method to add new question into our table"""
        print(question)
        a = "'" + "', '".join(question) + "'"
        print(a)
        try:
            self.cursor.execute(
                "INSERT OR IGNORE INTO '{table}' VALUES ({quest})".format(table=table, quest=a))
        except:
            self.cursor.execute(
                "INSERT OR IGNORE INTO '{table}' VALUES ('{quest}')".format(table=table, quest=question))
        self.conn.commit()
