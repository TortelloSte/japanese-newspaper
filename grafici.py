import os
import pandas as pd
import matplotlib.pyplot as plt


def apertura_file():
    lista_file = os.listdir('./data')
    csv_files = [file for file in lista_file if file.endswith('.csv')]

    print("File presenti:")
    for i, file in enumerate(csv_files, start=1):
        print(f"{i}. {file}")

    while True:
        selezione = input("Inserisci il numero del file da aprire (q per uscire): ")

        if selezione.lower() == 'q':
            return None

        if selezione.isdigit() and int(selezione) <= len(csv_files):
            selezionato = csv_files[int(selezione) - 1]
            file_path = os.path.join('./data', selezionato)
            try:
                df = pd.read_csv(file_path, sep='\t') 
                return df  
            except pd.errors.ParserError as e:
                print("Errore di lettura:", str(e))
            except pd.errors.EmptyDataError as e:
                print("Dataset vuoto:", str(e))
            except FileNotFoundError as e:
                print("File non trovato nella cartella:", str(e))
        else:
            print("Numero di file non valido. Riprova!")


df = apertura_file()
# mentre facevo le analisi ho pensato che potessero eserci dei duplicati quindi li controllo e nel caso rimuovo


def verifica_duplicati(df):
    duplicati = df.duplicated(subset=['text'], keep=False)
    if duplicati.any():
        print("Elementi duplicati")
        print(df[duplicati]['text'])
    else:
        print("No duplicati")

if df is not None:
    verifica_duplicati(df)

def rimuovi_duplicati(df):
    df_senza_duplicati = df.drop_duplicates(subset=['text'], keep='first')
    return df_senza_duplicati

if df is not None:
    df_senza_duplicati = rimuovi_duplicati(df)

print(df_senza_duplicati)

# ora vado a fare il grafico della colonna source prendendo i valori unici per vedere come sono i dati, e in quali quantita!

# da qui svolgerò le analisi solamente nel dataset japanese visto che in quello inglese ci sono solamente due case editrici con un dislivello enorme e quindi non ci sarebbe nulla da testare
