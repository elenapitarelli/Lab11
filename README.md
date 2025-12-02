# Lab 11

#### Argomenti

- Utilizzo di Grafi
- Utilizzo della libreria [NetworkX](https://networkx.org/)
- Visita e ricerca delle componenti connesse

---
> **❗ ATTENZIONE:** 
>  Ricordare di effettuare il **fork** del repository principale, quindi clonare su PyCharm il **repository personale** 
> (https://github.com/my-github-username/Lab11) e non quello principale.
> 
> In caso di dubbi consultare la guida caricata nel lab02: 
> https://github.com/Programmazione-Avanzata-2025-26/Lab02/blob/main/Guida.pdf

---

##  Gestione Sentieri di Montagna
In questo laboratorio si richiede di sviluppare un’applicazione Python dotata di interfaccia grafica che analizzi 
le connessioni tra i rifugi di montagna nel corso degli anni. I dati provengono dal database fornito, 
denominato `mountain_paths.sql`, che contiene le seguenti tabelle:

- `rifugio`: contiene le informazioni inerenti ai rifugi:
  - id
  - nome
  - localita
  - altitudine
  - capienza
  - aperto

- `connessione`: contiene le informazioni inerenti ai vari sentieri (un sentiero è una connessione
fra due rifugi):
  - id 
  - id_rifugio1
  - id_rifugio2
  - distanza (in km)
  - difficolta (facile, media, difficile)
  - durata (hh:mm:ss)
  - anno

![relazione_db.png](img/relazione_db.png)

---
##  Interfaccia
Nel progetto di base, l'interfaccia grafica (file `view.py` e `control.py`) è già implementata con il seguente layout:
![img.png](img/layout.png)
Tuttavia è possibile applicare modifiche se ritenuto necessario.

## ESERCIZIO 1: Costruzione del grafo dei sentieri
Considerare, per questo esercizio, solo la prima parte dell'interfaccia inerente al calcolo dei sentieri. 
L’applicazione deve permettere di: 
- Inserire un anno compreso tra 1950 e 2024 e premere il pulsante “Calcola sentieri”.
- Creare un grafo non orientato e non pesato che rappresenti la rete escursionistica fino all’anno indicato: 
  - I nodi rappresentano i rifugi collegati da almeno un sentiero fino all’anno selezionato. 
  - Gli archi rappresentano un sentiero escursionistico tra due rifugi.
- Stampare:
  - L’elenco dei rifugi, indicando per ciascuno il numero di rifugi collegati direttamente (grado del vertice).
  - Il numero di componenti connesse all’interno della rete di sentieri.

>💡 **Esempio di Funzionamento**: L’utente inserisce l'anno 1960 e clicca sul pulsante "Calcola Sentieri". Se l'anno 
> inserito ha un formato non valido o non appartenente all'intervallo indicato l'applicazione mostra un alert. 
> → il programma mostra il numero di componenti connesse del grafo creato e la lista dei nodi (i rifugi). Per ogni
> rifugio viene indicato il numero di vicini (grado del vertice)
![esercizio1.png](img/esercizio1.png)

## ESERCIZIO 2: Rifugi raggiungibili 
Partendo dal programma sviluppato nell’Esercizio 1, aggiungere la funzionalità “Rifugi raggiungibili”: 
Considerare, per questo esercizio, anche la seconda parte dell'interfaccia, la quale contiene:
- Un `Dropdown` per scegliere un rifugio tra quelli presenti nel grafo.
- Un `ElevatedButton` "Rifugi raggiungibili" per visualizzare i rifugi raggiungibili.
Facendo click sul pulsante, l'applicazione deve visualizzare in basso tutti i rifugi raggiungibili a partire dal rifugio 
selezionato. Questi rifugi corrispondono alla componente connessa associata al rifugio scelto.

### Tecniche possibili per la ricerca dei nodi raggiungibili
- **Metodi NetworkX**: `dfs_tree()`, `bfs_tree()` 
- **Algoritmo ricorsivo DFS** 
- **Algoritmo iterativo** con liste `visitati` e `da_visitare`:
  - Inizia inserendo il rifugio scelto in `da_visitare`
  - Estrae i nodi, aggiunge i vicini non visitati in `visitati`
  - Termina quando `da_visitare` è vuota 

❗❗❗ **ATTENZIONE**: testare almeno due tecniche per confronto. 

>💡 **Esempio di Funzionamento**: Dopo aver eseguito le istruzioni dell'Esercizio 1, l'utente seleziona il sentiero
> "Rifugio Aurora" dal dropdown, quindi clicca sul pulsante "Rifugi raggiungibili". → il programma mostra il 
> numero di rifugi raggiungibili a partire dal "Rifugio Aurora" e li elenca uno per uno.
![img.png](img/esercizio2.png)

## 💡 Suggerimenti Pratici
- Tutta la documentazione della libreria `NetworkX` è disponibile al seguente link: [`networkx_documentazione`](https://networkx.org/documentation/stable/#python).
- Funzioni utili: `nx.Graph()`, `dfs_tree()`, `bfs_tree()`, `neighbors()`, `connected_components()`
- Strutture dati utili per la risoluzione dell'algoritmo iterativo: `deque()` disponibile nel package 
[`collections`](https://docs.python.org/3/library/collections.html)

## Materiale Fornito
Il repository del Lab11 è organizzato con la struttura ad albero mostrata di seguito e contiene tutto il necessario per 
svolgere il laboratorio:

```code
Lab11/
├── database/
│   ├── __init__.py
|   ├── connector.cnf 
|   ├── DB_connect.py 
│   └── dao.py (DA MODIFICARE) 
│
├── model/ (AGGIUNGERE ULTERIORI CLASSI SE NECESSARIE) 
│   ├── __init__.py
│   └── model.py (DA MODIFICARE) 
│
├── UI/
│   ├── __init__.py
│   ├── alert.py
│   ├── controller.py
│   └── view.py
│
├── mountain_paths.sql (DA IMPORTARE)
└── main.py (DA ESEGUIRE)
 ```
