import pandas as pd
import sys
import os


def lista_data(funzione):
    def decoratore():
        lista_file = os.listdir('./data')
        csv_files = [file for file in lista_file if file.endswith('.csv')] # visto che sono in formato csv

        print("file presenti:")
        for i, file in enumerate(csv_files, start=1):
            print(f"{i}. {file}")

        while True: # in questo modo se si sbaglia non devo rieseguire il file ma lo richiede!
            selezione = input("file da utilizzare (q per uscire): ")

            if selezione.lower() == 'q': # cosi da mettere un metodo di uscita dal codice!
                sys.exit()

            if selezione.isdigit() and int(selezione) <= len(csv_files):
                selezionato = csv_files[int(selezione) - 1]
                file_path = os.path.join('./data', selezionato)
                try:
                    df = pd.read_csv(file_path, sep='\t') # alla fine questo è il codice classico di pandas per un csv
                    funzione(df) # qui si esegue la funzione
                except pd.errors.ParserError as e:
                    print("Errore di lettura", str(e)) # per cercare ulteriori errori
                except pd.errors.EmptyDataError as e:
                    print("Dataset vuoto", str(e)) # per cercare ulteriori errori
                except FileNotFoundError as e:
                    print("File non trovato nella cartella", str(e)) # per cercare ulteriori errori
            else:
                print("Hai sbagliato numero di file, riprova!")
    
    return decoratore # ora applico il decoratore sulla funzione che mi fa le analisi sul dataset che si seleziona


@lista_data
def analisi_dati(df):
     # print(df.head()) #
# usato come controllo per verificare che il dataset non fosse vuoto!

# ho analizzato il dataset con i controlli sulle righe
# per questo sto facendo in questo modo per la rimozione delle righe e colonne che non mi servono!
# visto che l'analisi serve solo tra testo e testata di giornale.

    colonne_da_eliminare = ["title", "date", "author"]
    colonne_presenti = [colonna for colonna in colonne_da_eliminare if colonna in df.columns]

    if colonne_presenti:
        df.drop(colonne_presenti, axis=1, inplace=True)
    
    valori_nulli = df[df.isnull().any(axis=1)]
    if not valori_nulli.empty:
        df.dropna(inplace=True)
    
    print(df.head(10))
    lunghezza_righe = len(df)
    print(lunghezza_righe)

    def verifica_duplicati(df):
        duplicati = df.duplicated(subset=['text'], keep=False)
        if duplicati.any():
            print("Elementi duplicati")
            print(df[duplicati]['text'])
        else:
            pass

    if df is not None:
        verifica_duplicati(df)

    def rimuovi_duplicati(df):
        df = df.drop_duplicates(subset=['text'], keep='first')
        return df

    if df is not None:
        df = rimuovi_duplicati(df)

    

    def analisi_per_ML(df):

        if not os.path.exists('grafici'):
            os.makedirs('grafici')
        
        conteggi = df['source'].value_counts().reset_index()
        conteggi.columns = ['Giornale', 'Conteggi']
        conteggi_file_path = 'grafici/conteggi_source.txt'
        conteggi.to_csv(conteggi_file_path, sep='\t', index=False)


    if df is not None:
        analisi_per_ML(df)


    if not os.path.exists('./data'):
        os.makedirs('./data')

    scelta = input("Vuoi salvare il dataset? (s/n): ")
    if scelta.lower() == "s":
        lingua = input("Inserisci la lingua (English/Japanese): ")
        lingua = lingua.lower()
        if lingua == "english":
            nome_file = "dataset_english.csv"
        elif lingua == "japanese":
            nome_file = "dataset_japanese.csv"
        else:
            print("Lingua non valida. Il dataset non sarà salvato.")
            return
        
        file_path = os.path.join('./data', nome_file)
        df.to_csv(file_path, sep='\t', index=False)
        print("Dataset salvato correttamente.")
    else:
        print("Il dataset non è stato salvato.")

analisi_dati() # questo fa si che si avvi la funzione decorata (ho scelto di usarla per allenarmi nel loro utilizzo :) XD