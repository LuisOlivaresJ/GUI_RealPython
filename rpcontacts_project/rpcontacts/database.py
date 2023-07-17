# -*- coding: utf-8 -*-
# rpcontacts/database.py

"""This module provides a database connection."""

from PySide6.QtWidgets import QMessageBox
from PySide6.QtSql import QSqlDatabase
from PySide6.QtSql import QSqlQuery

def createConnection(databaseName):
    """Create and open a database connection.

    Parameters
    ----------

    databaseName : str
        databaseName holds the name or path to the physical SQLite database file in your file system.
    """

    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning(
            None,
            "RP Contacts",
            f"Database Error: {connection.lastError().text()}",
        )
        return False
    _createContactsTable()
    return True

def _createContactsTable():
    """Create the contacts table in the databse."""
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
        Create TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name   VARCHAR(40) NOT NULL,
            job VARCHAR(50),
            email VARCHAR(40) NOT NULL
        )
        """
    )