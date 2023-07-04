# japanese-newspaper
https://www.kaggle.com/datasets/vyhuholl/japanese-newspapers-20052021

# utilizzo questo file per spiegare il codice:

nel file main.py sono state fatte differenti prove, notando alcuni errori nella lettura dei file in formato csv, probabilmente per un errore di divisione dal file principale che si può trovare all'interno di questa altra pagine di kaggle : https://www.kaggle.com/datasets/alvations/old-newspapers

Quindi ho deciso inizialmente di importare il file con le API di Kaggle, ma per comodità e per non inserire i dati personali delle API nella repo ho scelto la maniear tradizionale creando una cartella data, e inserendo i file, che sono però rimossi grazie al file .gitignore, quindi sono da scaricare e inserire manualmente all'interno della cartella data.

     I file che utilizzo per questa analisi e lo studio sono due, uno si chiama english_news.csv e l'altro japanese_news.csv. Su entrambi i dataset effettuerò le medesime analisi per trovare anche le differenze e allenare un modello per la comprensione del testo. Quindi il file presente nel main.py sarà generico per lo studio di entrambi, con la richiesta all'utente che utilizza il file di scegliere uno dei due!


Per far funzionare il codice serve importare nella propria macchina i seguenti pacchetti di python con pip
Aprire il prompt dei comandi > scrivere pip install os, sys, matplotlib, seaborn, pandas
    
# main.py

All'interno del file ho sviluppato una funzione che serve per leggere uno dei due dataset, questa semplice funzione permette la scelta di uno dei due dataset da analizzare, controlla che sia leggibile e invia in output il file, che viene estratto e inserito all'interno di una funzione decoratrice : @lista_data
* ho aggiunto un controllo approfondito sugli errori che potrebbero esserci nella lettura del dataset*
Questo permette di applicare questa funzione all'interno di una funzione esterna ossia: analisi_dati dove viene eseguita una analisi dettagliata dei dati presenti all'interno del dataset scelto. Il file viene dunque salvato nuovamente con tutti i dati che sono stati modificati.

# grafici.py

Nel codice vengono presi i nuovi dataset e andiamo a creare i grafici su misura.
Ho scelto di dividere i codici cosi da non avere tante righe di codice dentro lo stesso file

