import networkx as nx
from database.dao import DAO


class Model:
    def __init__(self):
        self.G = nx.Graph()

    def build_graph(self, year: int):
        """
        Costruisce il grafo (self.G) dei rifugi considerando solo le connessioni
        con campo `anno` <= year passato come argomento.
        Quindi il grafo avrà solo i nodi che appartengono almeno ad una connessione, non tutti quelli disponibili.
        :param year: anno limite fino al quale selezionare le connessioni da includere.
        """

        self.G.clear()
        lista_rifugi = DAO.read_rifugio()
        lista_connessioni = DAO.read_sentiero(year)

        for connessione in lista_connessioni:
            if connessione.anno <= year:
                print("Aggiungo arco", connessione.id_rifugio1, connessione.id_rifugio2)
                r1 = lista_rifugi[connessione.id_rifugio1]
                r2 = lista_rifugi[connessione.id_rifugio2]

                self.G.add_edge(r1, r2) # aggiunge nodi se non esistono gia
        return self.G



    def get_nodes(self):
        """
        Restituisce la lista dei rifugi presenti nel grafo.
        :return: lista dei rifugi presenti nel grafo.
        """

        lista_nodi = list(self.G.nodes())
        return lista_nodi

    def get_num_neighbors(self, node):
        """
        Restituisce il grado (numero di vicini diretti) del nodo rifugio.
        :param node: un rifugio (cioè un nodo del grafo)
        :return: numero di vicini diretti del nodo indicato
        """

        num_vicini = len(list(self.G.neighbors(node)))
        return num_vicini

    def get_num_connected_components(self):
        """
        Restituisce il numero di componenti connesse del grafo.
        :return: numero di componenti connesse
        """

        num_comp_connesse = int(nx.number_connected_components(self.G))
        return num_comp_connesse

    def get_reachable(self, start):
        """
        Deve eseguire almeno 2 delle 3 tecniche indicate nella traccia:
        * Metodi NetworkX: `dfs_tree()`, `bfs_tree()`
        * Algoritmo ricorsivo DFS
        * Algoritmo iterativo
        per ottenere l'elenco di rifugi raggiungibili da `start` e deve restituire uno degli elenchi calcolati.
        :param start: nodo di partenza, da non considerare nell'elenco da restituire.

        ESEMPIO
        a = self.get_reachable_bfs_tree(start)
        b = self.get_reachable_iterative(start)
        b = self.get_reachable_recursive(start)

        return a
        """

        # metodo 1 dfs_tree
        """tree = nx.dfs_tree(self.G, start)
        rifugi_raggiungibili = list(tree.nodes())
        rifugi_raggiungibili.remove(start)
        return rifugi_raggiungibili"""

        #metodo 2 dfs ricorsiva

        visitati = set()
        self.dfs_ricorsivo(start,visitati)

        visitati.remove(start)
        return visitati

    def dfs_ricorsivo(self,nodo,visitati):
        visitati.add(nodo)

        for vicino in self.G.neighbors(nodo):
            if vicino not in visitati:
                self.dfs_ricorsivo(vicino,visitati)



