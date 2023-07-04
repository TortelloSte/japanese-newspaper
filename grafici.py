import os
import pandas as pd

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
                df = pd.read_csv(file_path, sep='\t')  # Lettura del file CSV
                return df  # Restituisce il dataframe
            except pd.errors.ParserError as e:
                print("Errore di lettura:", str(e))
            except pd.errors.EmptyDataError as e:
                print("Dataset vuoto:", str(e))
            except FileNotFoundError as e:
                print("File non trovato nella cartella:", str(e))
        else:
            print("Numero di file non valido. Riprova!")

# Esempio di utilizzo
df = apertura_file()

print(df.head())