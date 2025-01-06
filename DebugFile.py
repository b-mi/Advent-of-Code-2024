class DebugFile:
    def __init__(self, file_path='debug.log'):
        """
        Inicializuje objekt DebugFile.

        :param file_path: Cesta k súboru, do ktorého sa bude zapisovať.
        """
        self.file_path = file_path

    def clear(self):
        """
        Vymaže obsah súboru.
        """
        with open(self.file_path, 'w') as file:
            pass  # Otvorí súbor v režime 'w' a hneď ho zavrie, čo vymaže obsah

    def print(self, text, end='\n'):
        """
        Zapíše text do súboru s možnosťou nastavenia ukončenia riadku.

        :param text: Text, ktorý sa má zapísať.
        :param end: Znak alebo reťazec, ktorý sa má pridať na koniec (defaultne '\n').
        """
        with open(self.file_path, 'a') as file:
            file.write(text + end)