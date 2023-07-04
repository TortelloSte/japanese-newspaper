# japanese-newspaper
https://www.kaggle.com/datasets/vyhuholl/japanese-newspapers-20052021

# utilizzo questo file per spiegare il codice:

nel file main.py sono state fatte differenti prove, notando alcuni errori nella lettura dei file in formato csv, probabilmente per un errore di divisione dal file principale che si può trovare all'interno di questa altra pagine di kaggle : https://www.kaggle.com/datasets/alvations/old-newspapers

Quindi ho deciso inizialmente di importare il file con le API di Kaggle, ma per comodità e per non inserire i dati personali delle API nella repo ho scelto la maniear tradizionale creando una cartella data, e inserendo i file, che sono però rimossi grazie al file .gitignore, quindi sono da scaricare e inserire manualmente all'interno della cartella data.

I file che utilizzo per questa analisi e lo studio sono due, uno si chiama english_news.csv e l'altro japanese_news.csv. Su entrambi i dataset effettuerò le medesime analisi per trovare anche le differenze e allenare un modello per la comprensione del testo. Quindi il file presente nel main.py sarà generico per lo studio di entrambi, con la richiesta all'utente che utilizza il file di scegliere uno dei due!


Per far funzionare il codice serve importare nella propria macchina i seguenti pacchetti di python con pip
Aprire il prompt dei comandi > scrivere pip install os, sys, matplotlib, seaborn, pandas

**Le analisi sono svolte solamente sul dataset Japanese_news.py visto che è l'unico con i dati che permettono vere analisi e applicazioni di ML**
# main.py

All'interno di questo file sono state fatte tutte le operazioni che portano ad avere il dataset pulito per i processi di analisi con il ML.
Il procedimento è molto facile, visto che ho fatto in modo che sia chiaro, e soprattutto il terminale giuida l'utente alle procedure da eseguire per poi passare al codice seguente grafici.py

# I grafici
Grafici maggiormente interessanti:
    migliore distribuzione nell'anno degli articoli
    grafico con chi ha fatto più articoli

Sono stati sviluppati i grafici su questi due fattori cosi da mostrare un po le distribusioni

# ML.py
