# IMPORTS

import mysql.connector as mysql



# DB CLASS

class BookManagerDB:
    """Class that connects to and disconnects from the database."""
    def __init__(self) -> None:
        """Constructor method."""
        # connect to the database using the host, user, password, and database arguments
        self.connection = mysql.connect(
            host = "127.0.0.1", 
            user = "root", 
            password = "password", 
            database = "bookmanager"
        )
    
    def get_cursor(self) -> mysql.cursor_cext.CMySQLCursor:
        """Method that returns a cursor object."""
        return self.connection.cursor()
    
    def commit(self) -> bool or Exception:
        """Method that commits changes to the database."""
        # try committing changes to the database
        try:
            self.connection.commit()
            return True
        except Exception as e:
            return e
    
    def close(self) -> bool or Exception:
        """Method that closes the connection to the database."""
        # try closing the connection to the database
        try:
            self.connection.close()
            return True
        except Exception as e:
            return e
