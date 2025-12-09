from database.DB_connect import DBConnect
from model.rifugio import Rifugio
from model.connessione import Connessione

class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    @staticmethod
    def read_rifugio():
        cnx= DBConnect.get_connection()
        result = {}
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM rifugio"
        cursor.execute(query)
        for row in cursor:
            rifugio = Rifugio(row["id"], row["nome"], row["localita"], row["altitudine"], row["capienza"], row["aperto"])
            result[rifugio.id] = rifugio

        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def read_sentiero(year):
        cnx= DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Sentiero non trovato")
            return None
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM connessione"

        cursor.execute(query)
        for row in cursor:
            connessione = Connessione(row["id"],row["id_rifugio1"], row["id_rifugio2"], row["distanza"],row["durata"],row["anno"])
            result.append(connessione)
        cursor.close()
        cnx.close()
        return result










