import os

def rename_files(directory):
    """
    Rinomina tutti i file in una cartella aggiungendo un numero incrementale a partire da 71.

    :param directory: Percorso della cartella contenente i file.
    """
    start_number = 71  # Numero iniziale
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        
        for i, filename in enumerate(files, start=start_number):
            # Estrai l'estensione del file
            file_extension = os.path.splitext(filename)[1]
            # Nuovo nome del file
            new_name = f"file_{i}{file_extension}"
            # Percorsi completi
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)
            # Rinomina il file
            os.rename(old_path, new_path)
            print(f"Rinominato: {filename} -> {new_name}")
        
        print("Rinominazione completata!")
    except Exception as e:
        print(f"Errore: {e}")

# Esempio di utilizzo
if __name__ == "__main__":
    directory_path = input("/home/jsorel/Desktop/nuovo_dataset/carta").strip()
    rename_files(directory_path)

