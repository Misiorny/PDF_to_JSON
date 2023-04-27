import PyPDF2
import json

# otwórz plik pdf w trybie binarnym
with open('JS.pdf', 'rb') as pdf_file: #pierwszy argument to nazwa pliku, który musi być w katalogu głównym
    # utwórz obiekt PdfFileReader
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # utwórz pustą listę, do której będziemy dodawać słowniki
    data = []

    # przejdź przez każdą stronę w pliku pdf
    for page_num in range(len(pdf_reader.pages)):
        # pobierz tekst z aktualnej strony
        page = pdf_reader.pages[page_num]
        page_text = page.extract_text()

        # utwórz słownik z tekstem i numerem strony
        page_dict = {
            'page_number': page_num,
            'text': page_text
        }

        # dodaj słownik do listy
        data.append(page_dict)

# otwórz plik json w trybie zapisu
with open('fiszkiJS.json', 'w') as json_file: #pierwszy argument to nazwa pliku json
    # zapisz listę słowników do pliku json
    json.dump(data, json_file)

